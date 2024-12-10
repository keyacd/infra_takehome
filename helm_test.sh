echo '***ATTEMPTING UNINSTALL***'
helm uninstall birds
echo '***RE-INSTALLING***'
helm install birds helm/birds
echo '***RUNNING TESTS***'
helm test birds --hide-notes