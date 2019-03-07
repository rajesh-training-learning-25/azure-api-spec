// <auto-generated>
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
//
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace Microsoft.Azure.PowerShell.Cmdlets.Peering.Models
{
    using Newtonsoft.Json;
    using System.Linq;

    /// <summary>
    /// The SKU that defines the tier and kind of the peering.
    /// </summary>
    public partial class PSPeeringSku
    {
        /// <summary>
        /// Initializes a new instance of the PSPeeringSku class.
        /// </summary>
        public PSPeeringSku()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the PSPeeringSku class.
        /// </summary>
        /// <param name="name">The name of the peering SKU. Possible values
        /// include: 'Basic_Exchange_Free', 'Basic_Direct_Free',
        /// 'Premium_Direct_Free', 'Premium_Exchange_Metered'</param>
        /// <param name="tier">The tier of the peering SKU. Possible values
        /// include: 'Basic', 'Premium'</param>
        /// <param name="family">The family of the peering SKU. Possible values
        /// include: 'Direct', 'Exchange'</param>
        /// <param name="size">The size of the peering SKU. Possible values
        /// include: 'Free', 'Metered', 'Unlimited'</param>
        public PSPeeringSku(string name = default(string), string tier = default(string), string family = default(string), string size = default(string))
        {
            Name = name;
            Tier = tier;
            Family = family;
            Size = size;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets the name of the peering SKU. Possible values include:
        /// 'Basic_Exchange_Free', 'Basic_Direct_Free', 'Premium_Direct_Free',
        /// 'Premium_Exchange_Metered'
        /// </summary>
        [JsonProperty(PropertyName = "name")]
        public string Name { get; set; }

        /// <summary>
        /// Gets or sets the tier of the peering SKU. Possible values include:
        /// 'Basic', 'Premium'
        /// </summary>
        [JsonProperty(PropertyName = "tier")]
        public string Tier { get; set; }

        /// <summary>
        /// Gets or sets the family of the peering SKU. Possible values
        /// include: 'Direct', 'Exchange'
        /// </summary>
        [JsonProperty(PropertyName = "family")]
        public string Family { get; set; }

        /// <summary>
        /// Gets or sets the size of the peering SKU. Possible values include:
        /// 'Free', 'Metered', 'Unlimited'
        /// </summary>
        [JsonProperty(PropertyName = "size")]
        public string Size { get; set; }

    }
}
