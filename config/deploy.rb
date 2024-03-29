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
            execute 'source /home/ubuntu/challenge/exporter_env/bin/activate'
            execute '/home/ubuntu/challenge/exporter_env/bin/pip install -r /home/ubuntu/challenge/fastapi-vizz-challenge/current/exporter/requirements.txt'
        end
        end
    end
    end

namespace :importer do
    desc "Deploy Importer"
    task :deploy do
        on roles(:app) do
        within '/home/ubuntu/challenge/fastapi-vizz-challenge/importer' do
            execute 'source /home/ubuntu/challenge/importer_env/bin/activate'
            execute '/home/ubuntu/challenge/importer_env/bin/pip install -r /home/ubuntu/challenge/fastapi-vizz-challenge/current/importer/requirements.txt'
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

namespace :deploy do
  desc 'Exporter Health Check'
  task :health_exporter do
    on roles(:app) do
      retry_count = 0
      max_retries = 5
      delay = 10

      while retry_count < max_retries
        if test "curl -s http://localhost:4000/ping | grep pong"
          info 'Exporter is Up!'
          break
        else
          retry_count += 1
          info "Waiting for Exporter to start (attempt #{retry_count})..."
          sleep delay
        end
      end

      if retry_count == max_retries
        error 'Exporter did not start in time!'
        exit 1
      end
    end
  end

  desc 'Importer Health Check'
  task :health_importer do
    on roles(:app) do
      retry_count = 0
      max_retries = 5
      delay = 10

      while retry_count < max_retries
        if test "curl -s http://localhost:3000/ping | grep pong"
          info 'Importer is Up!'
          break
        else
          retry_count += 1
          info "Waiting for Importer to start (attempt #{retry_count})..."
          sleep delay
        end
      end

      if retry_count == max_retries
        error 'Importer down...!'
        exit 1
      end
    end
  end
end

