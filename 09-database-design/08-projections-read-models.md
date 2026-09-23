# Projections and Read Models

> Status: **SUPPORTING PERSISTENCE ARCHITECTURE — CP7 DATA MODEL; NOT IMPLEMENTATION FREEZE**

```text
Canonical Truth → Projection / Read Model → UI / Search / Operational View
```

Authority never reverses. Use progressive strategy: direct query → view/derived query → persisted projection as complexity/performance requires. Availability remains derived; daily calendar rows, if used, are disposable projections. Search availability is advisory and final commitment revalidates canonical truth. Search/display price is not transaction price truth.

Host Dashboard is responsibility-oriented. Sale Earnings derives from Entitlement/Settlement/Payout. Butler Today exposes operational need-to-know only. Destination Today includes Stayora and External represented Stays; External Stay is not second-class operationally. Guest Stay Access is scoped/security-sensitive; QR projection does not replace authority. Reputation projections are audience-specific. Verification Summary derives from decision history. Admin Attention starts as a federated projection, not necessarily a Task aggregate.

Projection staleness is explicit. Sensitive commands revalidate canonical truth and projections never bypass authorization. V0 may use hybrid query-time, synchronous and asynchronous projections; no heavy CQRS infrastructure is required. PostgreSQL is default V0 read/search infrastructure. Operational Today uses Destination-local date.

`Searchability ≠ Inventory Availability ≠ Actor-specific Bookability`.
