class SpotifyDl < Formula
  include Language::Python::Virtualenv

  desc "Downloads songs from your Spotify Playlist"
  homepage "https://github.com/SathyaBhat/spotify-dl"
  url "https://github.com/SathyaBhat/spotify-dl/archive/refs/tags/v7.6.0.tar.gz"
  sha256 "e0ce32d3bc136a386770eef40025dd993d59311e6ee9daa9a038307c0f500b97"
  license "MIT"

  depends_on "python@3.9"

  resource "certifi" do
    url "https://files.pythonhosted.org/packages/6c/ae/d26450834f0acc9e3d1f74508da6df1551ceab6c2ce0766a593362d6d57f/certifi-2021.10.8.tar.gz"
    sha256 "78884e7c1d4b00ce3cea67b44566851c4343c120abd683433ce934a68ea58872"
  end

  resource "charset-normalizer" do
    url "https://files.pythonhosted.org/packages/eb/7f/a6c278746ddbd7094b019b08d1b2187101b1f596f35f81dc27f57d8fcf7c/charset-normalizer-2.0.6.tar.gz"
    sha256 "5ec46d183433dcbd0ab716f2d7f29d8dee50505b3fdb40c6b985c7c4f5a3591f"
  end

  resource "idna" do
    url "https://files.pythonhosted.org/packages/cb/38/4c4d00ddfa48abe616d7e572e02a04273603db446975ab46bbcd36552005/idna-3.2.tar.gz"
    sha256 "467fbad99067910785144ce333826c71fb0e63a425657295239737f7ecd125f3"
  end

  resource "mutagen" do
    url "https://files.pythonhosted.org/packages/f3/d9/2232a4cb9a98e2d2501f7e58d193bc49c956ef23756d7423ba1bd87e386d/mutagen-1.45.1.tar.gz"
    sha256 "6397602efb3c2d7baebd2166ed85731ae1c1d475abca22090b7141ff5034b3e1"
  end

  resource "peewee" do
    url "https://files.pythonhosted.org/packages/e1/3e/a21e7268fa39756cdbd6d86af78ff1c0a92b84d6dbfadff431e9e3b9e1d3/peewee-3.13.3.tar.gz"
    sha256 "1269a9736865512bd4056298003aab190957afe07d2616cf22eaf56cb6398369"
  end

  resource "requests" do
    url "https://files.pythonhosted.org/packages/e7/01/3569e0b535fb2e4a6c384bdbed00c55b9d78b5084e0fb7f4d0bf523d7670/requests-2.26.0.tar.gz"
    sha256 "b8aa58f8cf793ffd8782d3d8cb19e66ef36f7aba4353eec859e74678b01b07a7"
  end

  resource "sentry-sdk" do
    url "https://files.pythonhosted.org/packages/f4/02/04c32ee4f98b6cc46cad1daf22c65571ee87f35c272052abf4043c1a8a28/sentry-sdk-0.19.4.tar.gz"
    sha256 "1052f0ed084e532f66cb3e4ba617960d820152aee8b93fc6c05bd53861768c1c"
  end

  resource "six" do
    url "https://files.pythonhosted.org/packages/71/39/171f1c67cd00715f190ba0b100d606d440a28c93c7714febeca8b79af85e/six-1.16.0.tar.gz"
    sha256 "1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926"
  end

  resource "spotipy" do
    url "https://files.pythonhosted.org/packages/53/f0/d4605b887e01686d01dc1c1d25e8d13af8a12bf1dc1ed3c87e9bd909b49d/spotipy-2.16.1.tar.gz"
    sha256 "4564a6b05959deb82acc96a3fe6883db1ad9f8c73b7ff3b9f1f44db43feba0b8"
  end

  resource "urllib3" do
    url "https://files.pythonhosted.org/packages/80/be/3ee43b6c5757cabea19e75b8f46eaf05a2f5144107d7db48c7cf3a864f73/urllib3-1.26.7.tar.gz"
    sha256 "4987c65554f7a2dbf30c18fd48778ef124af6fab771a377103da0585e2336ece"
  end

  resource "youtube_dl" do
    url "https://files.pythonhosted.org/packages/c6/75/05979677d9abc76851d13d8db3951e39017ac223545adab6e8576fa0cbe7/youtube_dl-2021.6.6.tar.gz"
    sha256 "cb2d3ee002158ede783e97a82c95f3817594df54367ea6a77ce5ceea4772f0ab"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    # system "false"
    system "#{bin}/spotify-dl", "-h"
  end
end
