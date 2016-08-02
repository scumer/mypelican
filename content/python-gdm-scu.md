Title: Python GDCM SCU
Subtitle: [dicom scu]
Date: 2016-07-31
Category: Python
Tags: python, gdcm
Slug: python-gdcm-scu
Summary: program dicom scu with python gdcm
	
使用python gdcm编写dicom scu,c-find/c-move/c-store

	#!python
    def _getQuery(kwargs):
	    queryKeys = gdcm.DataSet()
	    for key in kwargs:
	        if key != studyUIDTag:
	            continue
	        de = gdcm.DataElement()
	        de.SetTag(key)
	        de.SetByteValue(kwargs[key],gdcm.VL(len(kwargs[key])))
	        queryKeys.Insert(de)

	    #ePatientRootType,eStudyRootType   # ePatient,eStudy,eSeries,eImage 
	    query = gdcm.CompositeNetworkFunctions_ConstructQuery(gdcm.eStudyRootType,gdcm.eStudy,queryKeys,True) 
	    return query

    scu = gdcm.ServiceClassUser()
    scu.SetHostname(MOVE_CONFIG['host'])
    scu.SetPort(MOVE_CONFIG['port'])
    scu.SetTimeout(100)
    scu.SetCalledAETitle(MOVE_CONFIG['callAE'])
    scu.SetAETitle(MOVE_CONFIG['callingAE'])
    scu.SetPortSCP(MOVE_CONFIG['retrievePort'])

    query = _getQuery(
        {
            studyUIDTag:studyUID,
            seriesUIDTag:seriesUID,
            sopUIDTag:sopUID
        })
    print 'query:', query.ValidateQuery()

    print 'InitializeConnection:', scu.InitializeConnection()
    generator = gdcm.PresentationContextGenerator()
    generator.GenerateFromUID(query.GetAbstractSyntaxUID())  # !!!
    scu.SetPresentationContexts(generator.GetPresentationContexts())

    if scu.StartAssociation():
        # print 'Echo:',scu.SendEcho()
        res = gdcm.DataSetArrayType()
        # if scu.SendFind(query, res):
        if scu.SendMove(query, MOVE_CONFIG['path']):
            pass
            # for dataset in res:
            #     print dataset.GetDataElement(studyUIDTag)
            #     print dataset.GetDataElement(seriesUIDTag)
            #     print dataset.GetDataElement(sopUIDTag)
        scu.StopAssociation()
