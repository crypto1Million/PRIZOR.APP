interface ProfileStatsProps {
  followers: number;
  following: number;
  posts: number;
  profileViews: number;
}

export default function ProfileStats({
  followers,
  following,
  posts,
  profileViews,
}: ProfileStatsProps) {
  return (
    <div className="flex gap-8 mt-4">
      <div>
        <div>{followers}</div>
        <div>Followers</div>
      </div>

      <div>
        <div>{following}</div>
        <div>Following</div>
      </div>

      <div>
        <div>{posts}</div>
        <div>Posts</div>
      </div>

      <div>
        <div>{profileViews}</div>
        <div>Profile Views</div>
      </div>
    </div>
  );
}