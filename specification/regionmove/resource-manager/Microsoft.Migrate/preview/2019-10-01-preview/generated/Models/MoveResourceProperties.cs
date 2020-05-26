// <auto-generated>
// MICROSOFT-MIT_NO_VERSION
// </auto-generated>

namespace regionmovecollection.Models
{
    using Newtonsoft.Json;
    using System.Collections;
    using System.Collections.Generic;
    using System.Linq;

    /// <summary>
    /// Defines the move resource properties.
    /// </summary>
    public partial class MoveResourceProperties
    {
        /// <summary>
        /// Initializes a new instance of the MoveResourceProperties class.
        /// </summary>
        public MoveResourceProperties()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the MoveResourceProperties class.
        /// </summary>
        /// <param name="provisioningState">Possible values include:
        /// 'Succeeded', 'Updating', 'Creating', 'Failed'</param>
        /// <param name="sourceId">Gets or sets the Source ARM Id of the
        /// resource.</param>
        /// <param name="targetId">Gets the Target ARM Id of the
        /// resource.</param>
        /// <param name="resourceSettings">Gets or sets the resource
        /// settings.</param>
        /// <param name="dependsOn">Gets or sets the move resource
        /// dependencies.</param>
        public MoveResourceProperties(string provisioningState = default(string), string sourceId = default(string), string targetId = default(string), ResourceSettings resourceSettings = default(ResourceSettings), MoveResourceStatus moveStatus = default(MoveResourceStatus), IList<MoveResourceDependency> dependsOn = default(IList<MoveResourceDependency>))
        {
            ProvisioningState = provisioningState;
            SourceId = sourceId;
            TargetId = targetId;
            ResourceSettings = resourceSettings;
            MoveStatus = moveStatus;
            DependsOn = dependsOn;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets possible values include: 'Succeeded', 'Updating',
        /// 'Creating', 'Failed'
        /// </summary>
        [JsonProperty(PropertyName = "provisioningState")]
        public string ProvisioningState { get; set; }

        /// <summary>
        /// Gets or sets the Source ARM Id of the resource.
        /// </summary>
        [JsonProperty(PropertyName = "sourceId")]
        public string SourceId { get; set; }

        /// <summary>
        /// Gets the Target ARM Id of the resource.
        /// </summary>
        [JsonProperty(PropertyName = "targetId")]
        public string TargetId { get; private set; }

        /// <summary>
        /// Gets or sets the resource settings.
        /// </summary>
        [JsonProperty(PropertyName = "resourceSettings")]
        public ResourceSettings ResourceSettings { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "moveStatus")]
        public MoveResourceStatus MoveStatus { get; set; }

        /// <summary>
        /// Gets or sets the move resource dependencies.
        /// </summary>
        [JsonProperty(PropertyName = "dependsOn")]
        public IList<MoveResourceDependency> DependsOn { get; set; }

    }
}
