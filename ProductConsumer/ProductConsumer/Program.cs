using System;
using System.Text.Json;
using System.Threading;
using Confluent.Kafka;
using Nest;

namespace ProductConsumer
{
    static class Program
    {
        private static readonly JsonSerializerOptions SerializerOptions = new JsonSerializerOptions {PropertyNameCaseInsensitive = true};

        public static void Main()
        {
            var client = new ElasticClient(new ConnectionSettings(new Uri("http://elastic:changeme@localhost:9200")));

            using var c = new ConsumerBuilder<Ignore, string>(new ConsumerConfig
            { 
                GroupId = "test-consumer-group",
                BootstrapServers = "localhost:9092",
                AutoOffsetReset = AutoOffsetReset.Earliest
            }).Build();
            
            c.Subscribe("enhanced_products");
            
            Console.WriteLine("Consumer is ready");
            SendProducts(c, client);
        }

        private static void SendProducts(IConsumer<Ignore, string> c, ElasticClient client)
        {
            try
            {
                var cts = new CancellationTokenSource();
                Console.CancelKeyPress += (_, e) =>
                {
                    e.Cancel = true;
                    cts.Cancel();
                };

                while (true)
                {
                    try
                    {
                        var cr = c.Consume(cts.Token);
                        var product = JsonSerializer.Deserialize<ProductDto>(cr.Value, SerializerOptions);

                        client.Index(product, i => i.Index("products"));
                    }
                    catch (ConsumeException e)
                    {
                        Console.WriteLine($"Error occured: {e.Error.Reason}");
                    }
                }
            }
            catch (OperationCanceledException)
            {
                c.Close();
            }
        }
    }
}