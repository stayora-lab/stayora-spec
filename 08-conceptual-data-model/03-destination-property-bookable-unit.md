# Destination, Property and Bookable Unit

> Status: **STABLE — CP7 ARCHITECTURE REVIEWED; NOT IMPLEMENTATION FREEZE**

```text
Destination → Property → Bookable Unit
```

Destination is a business and operational boundary, not merely a geographic filter. Property identifies an accommodation asset/listing. Bookable Unit identifies the resource that can be committed for a time range. Inventory belongs to `Bookable Unit + Time`, not a UI page, channel or generic Property status.

For Oceanami V0, one Villa is conceptually one Property plus one Entire-Villa Bookable Unit. The UI may simply call it “Villa”. Nested inventory such as Entire Villa plus individual bedrooms is OUT OF SCOPE — V0.

Destination Membership is separate from ownership, publication, Verification and Inventory Availability. Destination-specific capabilities remain configuration/policy and do not silently become universal Core requirements.
