using System.Collections.Generic;

namespace ProductConsumer
{
    public class ProductDto
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public IEnumerable<string> ImageUrls { get; set; }
        public string Sku { get; set; }
        public string Brand { get; set; }
        public int CreatedAt { get; set; }
        public int UpdatedAt { get; set; }
        public string ShortDescription { get; set; }
    }
}