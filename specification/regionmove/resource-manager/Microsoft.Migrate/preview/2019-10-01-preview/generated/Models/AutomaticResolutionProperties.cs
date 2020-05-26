// <auto-generated>
// MICROSOFT-MIT_NO_VERSION
// </auto-generated>

namespace regionmovecollection.Models
{
    using Newtonsoft.Json;
    using System.Linq;

    /// <summary>
    /// Defines the properties for automatic resolution.
    /// </summary>
    public partial class AutomaticResolutionProperties
    {
        /// <summary>
        /// Initializes a new instance of the AutomaticResolutionProperties
        /// class.
        /// </summary>
        public AutomaticResolutionProperties()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the AutomaticResolutionProperties
        /// class.
        /// </summary>
        /// <param name="moveResourceId">Gets the MoveResource ARM ID of
        /// the dependent resource if the resolution type is Automatic.</param>
        public AutomaticResolutionProperties(string moveResourceId = default(string))
        {
            MoveResourceId = moveResourceId;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets the MoveResource ARM ID of
        /// the dependent resource if the resolution type is Automatic.
        /// </summary>
        [JsonProperty(PropertyName = "moveResourceId")]
        public string MoveResourceId { get; set; }

    }
}
