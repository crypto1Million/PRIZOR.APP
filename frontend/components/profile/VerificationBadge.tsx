import { CheckCircle } from "lucide-react";

interface VerificationBadgeProps {
  verificationType?: "blue" | "pink" | null;
}

export default function VerificationBadge({
  verificationType,
}: VerificationBadgeProps) {
  if (!verificationType) return null;

  return (
    <CheckCircle
      className={`w-5 h-5 ${
        verificationType === "blue"
          ? "text-blue-500"
          : "text-pink-500"
      }`}
    />
  );
}