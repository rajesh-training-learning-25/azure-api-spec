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
    /// Defines values for Gender.
    /// </summary>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum Gender
    {
        [EnumMember(Value = "male")]
        Male,
        [EnumMember(Value = "female")]
        Female,
        [EnumMember(Value = "genderless")]
        Genderless
    }
    internal static class GenderEnumExtension
    {
        internal static string ToSerializedValue(this Gender? value)
        {
            return value == null ? null : ((Gender)value).ToSerializedValue();
        }

        internal static string ToSerializedValue(this Gender value)
        {
            switch( value )
            {
                case Gender.Male:
                    return "male";
                case Gender.Female:
                    return "female";
                case Gender.Genderless:
                    return "genderless";
            }
            return null;
        }

        internal static Gender? ParseGender(this string value)
        {
            switch( value )
            {
                case "male":
                    return Gender.Male;
                case "female":
                    return Gender.Female;
                case "genderless":
                    return Gender.Genderless;
            }
            return null;
        }
    }
}
