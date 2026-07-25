source "https://rubygems.org"

# Use local theme gem for testing
gem "minimal-mistakes-jekyll", path: "./"

group :jekyll_plugins do
  gem "jekyll-algolia", "~> 1.0"
  gem "jekyll-postfiles"
  gem "jekyll-leaflet"
  gem 'faraday-retry'
end

gem "webrick"                      # Required for Ruby 3.x and up

# Windows-only file watcher
# gem "wdm", "~> 0.1.0" if Gem.win_platform?

# Explicitly include stdlib gems that will be removed in Ruby 3.4+
gem "csv"
gem "base64"
gem "bigdecimal"
gem "mutex_m"

# Ensure compatibility with Jekyll SCSS pipeline
gem "jekyll-sass-converter", "~> 2.2.0"