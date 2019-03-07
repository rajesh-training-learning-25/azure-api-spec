// <auto-generated>
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace Microsoft.Azure.Management.Peering.Models
{
    using Newtonsoft.Json;
    using System.Collections;
    using System.Collections.Generic;
    using System.Linq;

    /// <summary>
    /// The properties that define a direct peering location.
    /// </summary>
    public partial class PeeringLocationPropertiesDirect
    {
        /// <summary>
        /// Initializes a new instance of the PeeringLocationPropertiesDirect
        /// class.
        /// </summary>
        public PeeringLocationPropertiesDirect()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the PeeringLocationPropertiesDirect
        /// class.
        /// </summary>
        /// <param name="peeringFacilities">The list of direct peering
        /// facilities at the peering location.</param>
        /// <param name="bandwidthOffers">The list of bandwidth offers avaiable
        /// at the peering location.</param>
        public PeeringLocationPropertiesDirect(IList<DirectPeeringFacility> peeringFacilities = default(IList<DirectPeeringFacility>), IList<PeeringBandwidthOffer> bandwidthOffers = default(IList<PeeringBandwidthOffer>))
        {
            PeeringFacilities = peeringFacilities;
            BandwidthOffers = bandwidthOffers;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets the list of direct peering facilities at the peering
        /// location.
        /// </summary>
        [JsonProperty(PropertyName = "peeringFacilities")]
        public IList<DirectPeeringFacility> PeeringFacilities { get; set; }

        /// <summary>
        /// Gets or sets the list of bandwidth offers avaiable at the peering
        /// location.
        /// </summary>
        [JsonProperty(PropertyName = "bandwidthOffers")]
        public IList<PeeringBandwidthOffer> BandwidthOffers { get; set; }

    }
}
