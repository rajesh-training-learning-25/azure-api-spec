// <auto-generated>
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
//
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace Microsoft.Azure.CognitiveServices.Vision.Face.Models
{
    using Newtonsoft.Json;
    using Newtonsoft.Json.Converters;
    using System.Runtime;
    using System.Runtime.Serialization;

    /// <summary>
    /// Defines values for HairColorType.
    /// </summary>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum HairColorType
    {
        [EnumMember(Value = "unknown")]
        Unknown,
        [EnumMember(Value = "white")]
        White,
        [EnumMember(Value = "gray")]
        Gray,
        [EnumMember(Value = "blond")]
        Blond,
        [EnumMember(Value = "brown")]
        Brown,
        [EnumMember(Value = "red")]
        Red,
        [EnumMember(Value = "black")]
        Black,
        [EnumMember(Value = "other")]
        Other
    }
    internal static class HairColorTypeEnumExtension
    {
        internal static string ToSerializedValue(this HairColorType? value)
        {
            return value == null ? null : ((HairColorType)value).ToSerializedValue();
        }

        internal static string ToSerializedValue(this HairColorType value)
        {
            switch( value )
            {
                case HairColorType.Unknown:
                    return "unknown";
                case HairColorType.White:
                    return "white";
                case HairColorType.Gray:
                    return "gray";
                case HairColorType.Blond:
                    return "blond";
                case HairColorType.Brown:
                    return "brown";
                case HairColorType.Red:
                    return "red";
                case HairColorType.Black:
                    return "black";
                case HairColorType.Other:
                    return "other";
            }
            return null;
        }

        internal static HairColorType? ParseHairColorType(this string value)
        {
            switch( value )
            {
                case "unknown":
                    return HairColorType.Unknown;
                case "white":
                    return HairColorType.White;
                case "gray":
                    return HairColorType.Gray;
                case "blond":
                    return HairColorType.Blond;
                case "brown":
                    return HairColorType.Brown;
                case "red":
                    return HairColorType.Red;
                case "black":
                    return HairColorType.Black;
                case "other":
                    return HairColorType.Other;
            }
            return null;
        }
    }
}
