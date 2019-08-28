import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [  #before run introducing prescaling for jetTriggers (135445)
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/12C82F09-148F-E811-8447-0CC47A4C8EB6.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/9296F95B-128F-E811-B7A5-0025905B855A.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/10E5279D-1C8F-E811-B98B-0CC47A4D7626.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/B6F51F07-138F-E811-A262-0025905B8598.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/56251E6C-038F-E811-9EE2-0025905B85BC.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/6A21F2E5-048F-E811-BF6D-0025905B8592.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/9E00E1AB-198F-E811-B87C-0CC47A78A3EC.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/7CD66B6A-038F-E811-995D-0CC47A4C8E16.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/CAB2DC35-068F-E811-A661-0CC47A78A440.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/98055413-048F-E811-BDF5-0CC47A4D7630.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/7E0C7F6F-088F-E811-967B-003048FFD71C.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/90621904-038F-E811-9203-0025905A607E.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/BC77782E-068F-E811-BDA3-0CC47A7452D0.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/76D21110-038F-E811-BD7C-0CC47A4D7600.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/BEA35507-188F-E811-9584-0CC47A4C8E56.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/12175923-188F-E811-BB33-0025905A48BC.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/16CCB61C-038F-E811-8607-0025905B85BA.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/90B13249-148F-E811-9346-0025905B8590.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/3C6541A5-178F-E811-9CBF-0025905A607E.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/E0FC671A-048F-E811-A4E3-0CC47A745282.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/0A61903A-148F-E811-A637-0025905A60B8.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/043B2A25-078F-E811-90A4-0CC47A78A440.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/42F2B31E-078F-E811-9A27-0CC47A78A418.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/3A7C9876-168F-E811-98DD-0025905B856E.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/E62D5723-0C8F-E811-B51B-0CC47A7C3432.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/BA1019AC-058F-E811-876E-0CC47A4D7662.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/9E3D814C-148F-E811-AE9A-0025905B857A.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/4014010F-188F-E811-8DAF-0CC47A74524E.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/5AF612CE-048F-E811-A5BC-0CC47A4D7662.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/0A2BBD01-018F-E811-8DFA-0CC47A78A4B0.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/8C8CD1F9-108F-E811-9FA4-0025905A607E.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/DCFA1211-188F-E811-8816-0025905B858A.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/F2E9247D-8A8F-E811-BAE2-0025905A60BE.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/9AE78256-128F-E811-9DE9-0025905A48F2.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/AA0A2582-FD8E-E811-8070-0CC47A78A2F6.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/AA7247BB-168F-E811-A035-0CC47A7C34C8.root',
'/store/relval/CMSSW_10_2_0/JetHT/RAW-RECO/JetHTJetPlusHOFilter-102X_dataRun2_PromptLike_v4_RelVal_jetHT2018B-v1/10000/5EC6061B-188F-E811-9C7F-0025905B856E.root'
#'/store/relval/CMSSW_11_0_0_pre5/RelValTTbar_13/GEN-SIM-RECO/110X_mcRun2_asymptotic_v2-v1/20000/C9E4D58A-0C73-5044-96E9-A333DA3DB2B8.root',
#'/store/relval/CMSSW_11_0_0_pre5/RelValTTbar_13/GEN-SIM-RECO/110X_mcRun2_asymptotic_v2-v1/20000/D3102E91-5296-6148-8075-4EE457F5C226.root'
]);

secFiles.extend( [ ]);

process = cms.Process("IpResiduals")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 5000

# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.EventContent.EventContent_cff')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = '102X_dataRun2_PromptLike_v4'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = source

#======================================
# HLT
#======================================
process.HLTMinBias = cms.EDFilter("HLTHighLevel",
                                  TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                  #HLTPaths = cms.vstring('HLT_L1_BscMinBiasOR_BptxPlusORMinus'),
                                  HLTPaths = cms.vstring('HLT_*'),
                                  eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
                                  andOr = cms.bool(True),              # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
                                  throw = cms.bool(True)               # throw exception on unknown path names
                                  )


# process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
# # remove the following lines if you run on RECO files
# process.TrackRefitter.src = 'generalTracks'
# process.TrackRefitter.NavigationSchool = ''

## PV refit
# process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
# from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import offlinePrimaryVertices
# process.offlinePrimaryVerticesFromRefittedTrks  = offlinePrimaryVertices.clone()
# process.offlinePrimaryVerticesFromRefittedTrks.TrackLabel                                       = cms.InputTag("TrackRefitter")
# process.offlinePrimaryVerticesFromRefittedTrks.vertexCollections.maxDistanceToBeam              = 1
# process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.maxNormalizedChi2             = 20
# process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.minSiliconLayersWithHits      = 5
# process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.maxD0Significance             = 5.0
# process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.minPixelLayersWithHits        = 2

process.load('IpResoStudies.EDAnalyzers.residuals_cfi')
#process.residuals.TrackLabel = cms.InputTag("TrackRefitter")
#process.residuals.VertexLabel = cms.InputTag("offlinePrimaryVerticesFromRefittedTrks")

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("output.root"),
                                   closeFileFast = cms.untracked.bool(True)
                                   )

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.p = cms.Path(#process.HLTMinBias*
    # process.offlineBeamSpot                        +
    # process.TrackRefitter                          +
    # process.offlinePrimaryVerticesFromRefittedTrks +
    process.residuals
)
