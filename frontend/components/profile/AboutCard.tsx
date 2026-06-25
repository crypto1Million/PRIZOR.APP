interface AboutCardProps {
  headline?: string;
  location?: string;
  occupation?: string;
  tradingRole?: string;
  currentMission?: string;
}

export default function AboutCard({
  headline,
  location,
  occupation,
  tradingRole,
  currentMission,
}: AboutCardProps) {
  return (
    <div
      className="
        bg-zinc-900
        border
        border-zinc-800
        rounded-2xl
        p-6
        mt-6
      "
    >
      <h2 className="text-xl font-bold text-white mb-6">
        About
      </h2>

      <div className="space-y-4">

        {headline && (
          <div className="flex items-center gap-3">
            <span className="text-xl">🚀</span>
            <span className="text-gray-300">
              {headline}
            </span>
          </div>
        )}

        {location && (
          <div className="flex items-center gap-3">
            <span className="text-xl">📍</span>
            <span className="text-gray-300">
              {location}
            </span>
          </div>
        )}

        {occupation && (
          <div className="flex items-center gap-3">
            <span className="text-xl">💼</span>
            <span className="text-gray-300">
              {occupation}
            </span>
          </div>
        )}

        {tradingRole && (
          <div className="flex items-center gap-3">
            <span className="text-xl">📈</span>
            <span className="text-gray-300">
              {tradingRole}
            </span>
          </div>
        )}

        {currentMission && (
          <div className="flex items-center gap-3">
            <span className="text-xl">🎯</span>
            <span className="text-gray-300">
              {currentMission}
            </span>
          </div>
        )}

      </div>
    </div>
  );
}