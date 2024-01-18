# config valid for current version and patch releases of Capistrano
lock "~> 3.18.0"

set :application, "fastapi_vizz_challenge"
set :repo_url, "https://github.com/alexeh/fastapi-vizz-challenge"
set :branch, "main"

# Default branch is :master
# ask :branch, `git rev-parse --abbrev-ref HEAD`.chomp

# Default deploy_to directory is /var/www/my_app_name
# set :deploy_to, "/var/www/my_app_name"

# Default value for :format is :airbrussh.
# set :format, :airbrussh

# You can configure the Airbrussh format using :format_options.
# These are the defaults.
# set :format_options, command_output: true, log_file: "log/capistrano.log", color: :auto, truncate: :auto

# Default value for :pty is false
# set :pty, true

# Default value for :linked_files is []
# append :linked_files, "config/database.yml", 'config/master.key'

# Default value for linked_dirs is []
# append :linked_dirs, "log", "tmp/pids", "tmp/cache", "tmp/sockets", "public/system", "vendor", "storage"

# Default value for default_env is {}
# set :default_env, { path: "/opt/ruby/bin:$PATH" }

# Default value for local_user is ENV['USER']
# set :local_user, -> { `git config user.name`.chomp }

# Default value for keep_releases is 5
# set :keep_releases, 5

# Uncomment the following to require manually verifying the host key before first deploy.
# set :ssh_options, verify_host_key: :secure

namespace :exporter do
    desc "Deploy Exporter"
    task :deploy do
        on roles(:app) do
        within '/home/ubuntu/challenge/fastapi-vizz-challenge/exporter' do
            execute 'source /home/ubuntu/challenge/fastapi-vizz-challenge/exporter/exporter_env/bin/activate'
            execute '/home/ubuntu/challenge/fastapi-vizz-challenge/exporter/exporter_env/bin/pip install -r /home/ubuntu/challenge/fastapi-vizz-challenge/exporter/requirements.txt'
        end
        end
    end
    end

namespace :importer do
    desc "Deploy Importer"
    task :deploy do
        on roles(:app) do
        within '/home/ubuntu/challenge/fastapi-vizz-challenge/importer' do
            execute 'source /home/ubuntu/challenge/fastapi-vizz-challenge/importer/importer_env/bin/activate'
            execute '/home/ubuntu/challenge/fastapi-vizz-challenge/importer/importer_env/bin/pip install -r /home/ubuntu/challenge/fastapi-vizz-challenge/importer/requirements.txt'
        end
        end
    end
    end


namespace :deploy do
  task :restart_services do
    on roles(:app) do
      execute "sudo systemctl restart exporter.service"
      execute "sudo systemctl restart importer.service"
    end
  end
end


