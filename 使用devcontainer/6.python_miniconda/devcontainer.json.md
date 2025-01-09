FROM mcr.microsoft.com/devcontainers/miniconda:1-3

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
#COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
#RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
#   && rm -rf /tmp/conda-tmp

#預設conda安裝的版本,安裝pipx,並把先前安裝的版本移除
RUN conda install -y python=3.11 \
    && pip install --no-cache-dir pipx \
    && pipx reinstall-all


#copy ../requirements.txt* 的所有檔案至容器的/tmp/pip-tmp/資料夾內,如果沒有../requirements.txt,就copy noop.txt至/tmp/pip-tmp 
COPY ../requirements.txt* .devcontainer/noop.txt /tmp/pip-tmp/

#if的語法是bash 語法:如果有這個檔,就安裝/tmp/pip-tmp/requirements.txt內的檔案,安裝完成後刪除/tmp/pip-tmp
RUN if [ -f "/tmp/pip-tmp/requirements.txt" ]; then \
        pip install -r /tmp/pip-tmp/requirements.txt; \
    fi \
    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>