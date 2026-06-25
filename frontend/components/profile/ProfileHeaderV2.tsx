"use client";

import Image from "next/image";
import VerificationBadge from "./VerificationBadge";
import ProfileStats from "./ProfileStats";
import ProfileBanner from "./ProfileBanner";

interface ProfileHeaderProps {

  fullName: string;

  username: string;

  bio?: string;

  location?: string;

  avatarUrl: string;

  bannerUrl?: string;

  verificationType?: "blue" | "pink" | null;

  followers: number;

  following: number;

  posts: number;

  profileViews: number;
}

export default function ProfileHeaderV2({
  fullName,
  username,
  bio,
  location,
  avatarUrl,
  bannerUrl,
  verificationType,
  followers,
  following,
  posts,
  profileViews,
}: ProfileHeaderProps) {
  return (
    <div className="bg-zinc-900 rounded-2xl overflow-hidden border border-zinc-800">

      <ProfileBanner
        bannerUrl={bannerUrl}
      />

      <div className="px-6 pb-6">

        <div className="-mt-16 flex flex-col md:flex-row md:items-end md:justify-between">

          <div>

            <Image
              src={avatarUrl}
              alt={fullName}
              width={128}
              height={128}
              className="
                rounded-full
                border-4
                border-zinc-900
                object-cover
              "
            />

            <div className="flex items-center gap-2 mt-4">

              <h1 className="text-3xl font-bold text-white">
                {fullName}
              </h1>

              <VerificationBadge
                verificationType={verificationType}
              />

            </div>

            <p className="text-gray-400">
              @{username}
            </p>

            {location && (
              <p className="text-gray-500 mt-1">
                📍 {location}
              </p>
            )}

            {bio && (
              <p className="text-gray-300 mt-3 max-w-2xl">
                {bio}
              </p>
            )}
          </div>

          <button
            className="
              mt-4
              md:mt-0
              px-6
              py-2
              rounded-xl
              bg-pink-600
              hover:bg-pink-500
              text-white
              font-semibold
            "
          >
            Edit Profile
          </button>

        </div>

        <ProfileStats
          followers={followers}
          following={following}
          posts={posts}
          profileViews={profileViews}
        />

      </div>

    </div>
  );
}