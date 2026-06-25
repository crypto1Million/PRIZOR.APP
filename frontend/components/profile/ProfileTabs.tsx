"use client";

import { useState } from "react";

type TabType =
  | "posts"
  | "photos"
  | "videos"
  | "communities"
  | "events"
  | "streams"
  | "about";

interface ProfileTabsProps {
  onTabChange?: (tab: TabType) => void;
}

const tabs: {
  key: TabType;
  label: string;
}[] = [
  {
    key: "posts",
    label: "Posts",
  },
  {
    key: "photos",
    label: "Photos",
  },
  {
    key: "videos",
    label: "Videos",
  },
  {
    key: "communities",
    label: "Communities",
  },
  {
    key: "events",
    label: "Events",
  },
  {
    key: "streams",
    label: "Streams",
  },
  {
    key: "about",
    label: "About",
  },
];

export default function ProfileTabs({
  onTabChange,
}: ProfileTabsProps) {
  const [activeTab, setActiveTab] =
    useState<TabType>("posts");

  const handleTabChange = (
    tab: TabType
  ) => {
    setActiveTab(tab);

    if (onTabChange) {
      onTabChange(tab);
    }
  };

  return (
    <div
      className="
      bg-zinc-900
      border
      border-zinc-800
      rounded-xl
      mt-6
      overflow-x-auto
    "
    >
      <div className="flex min-w-max">

        {tabs.map((tab) => (
          <button
            key={tab.key}
            onClick={() =>
              handleTabChange(tab.key)
            }
            className={`
              px-6
              py-4
              text-sm
              font-semibold
              transition-all
              border-b-2

              ${
                activeTab === tab.key
                  ? `
                    text-pink-500
                    border-pink-500
                    bg-zinc-800
                  `
                  : `
                    text-gray-400
                    border-transparent
                    hover:text-white
                    hover:bg-zinc-800
                  `
              }
            `}
          >
            {tab.label}
          </button>
        ))}
      </div>
    </div>
  );
}