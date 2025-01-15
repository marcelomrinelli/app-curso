#!/bin/bash
cd /workspaces/app-curso
source myenv/bin/activate
streamlit run appstreamlit.py --server.enableCORS false --server.enableXsrfProtection false
