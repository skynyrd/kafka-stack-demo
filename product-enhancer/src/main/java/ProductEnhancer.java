import com.google.gson.Gson;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.KStream;

import java.util.Collections;
import java.util.Properties;


public class ProductEnhancer {
    public static void main(String[] args) {
        Gson gson = new Gson();

        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "product-enhancer");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

        StreamsBuilder builder = new StreamsBuilder();
        KStream<String, String> textLines = builder.stream("test-topic");

        KStream<String, String> upperJson = textLines
                .mapValues(textLine -> {

                    Product p = gson.fromJson(textLine, Product.class);

                    p.updatedAt = (int) (System.currentTimeMillis() / 1000L);
                    p.imageUrls = Collections.singletonList("http://" + p.sku + ".com");
                    p.shortDescription = p.description.substring(0, 10);

                    return gson.toJson(p);
                });

        upperJson.to("output-test");

        KafkaStreams streams = new KafkaStreams(builder.build(), props);
        streams.start();
    }
}
