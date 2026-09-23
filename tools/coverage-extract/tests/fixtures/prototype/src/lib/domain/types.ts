export type StayStatus =
  | "SCHEDULED"
  | "COMPLETED";
export type PaymentOutcome = "SUCCEEDED" | "UNKNOWN";
export type Booking = {
  status: "CONFIRMED" | "CANCELLED";
};
