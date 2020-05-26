// <auto-generated>
// MICROSOFT-MIT_NO_VERSION
// </auto-generated>

namespace regionmovecollection.Models
{
    using Newtonsoft.Json;
    using System.Linq;

    /// <summary>
    /// Defines the properties for manual resolution.
    /// </summary>
    public partial class ManualResolutionProperties
    {
        /// <summary>
        /// Initializes a new instance of the ManualResolutionProperties class.
        /// </summary>
        public ManualResolutionProperties()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the ManualResolutionProperties class.
        /// </summary>
        /// <param name="targetId">Gets or sets the target resource ARM ID of
        /// the dependent resource if the resource type is Manual.</param>
        public ManualResolutionProperties(string targetId = default(string))
        {
            TargetId = targetId;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets the target resource ARM ID of the dependent resource
        /// if the resource type is Manual.
        /// </summary>
        [JsonProperty(PropertyName = "targetId")]
        public string TargetId { get; set; }

    }
}
