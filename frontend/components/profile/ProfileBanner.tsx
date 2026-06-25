interface ProfileBannerProps {
  bannerUrl?: string;
}

export default function ProfileBanner({
  bannerUrl,
}: ProfileBannerProps) {
  return (
    <div
      className="h-56 w-full rounded-xl bg-cover bg-center"
      style={{
        backgroundImage: bannerUrl
          ? `url(${bannerUrl})`
          : undefined,
      }}
    />
  );
}