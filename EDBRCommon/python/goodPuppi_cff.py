import FWCore.ParameterSet.Config as cms
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector

goodPuppi = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                        filterParams = pfJetIDSelector.clone(),
                        src = cms.InputTag("slimmedJetsAK8")
                        )



### Cleaning
# We want to make sure that the jets are not the electrons or muons done previously

import PhysicsTools.PatAlgos.cleaningLayer1.jetCleaner_cfi as jetCleaner_cfi

cleanPuppi = jetCleaner_cfi.cleanPatJets.clone()
cleanPuppi.src = "goodPuppi"
#cleanJets.src = "slimmedJetsAK8"
cleanPuppi.checkOverlaps.muons.src = "goodMuons"
cleanPuppi.checkOverlaps.muons.deltaR = 1.0
#cleanJets.checkOverlaps.muons.deltaR = 0.
cleanPuppi.checkOverlaps.muons.requireNoOverlaps = True
cleanPuppi.checkOverlaps.electrons.src = "goodElectrons"
cleanPuppi.checkOverlaps.electrons.deltaR = 1.0
#cleanJets.checkOverlaps.electrons.deltaR = 0.
cleanPuppi.checkOverlaps.electrons.requireNoOverlaps = True
cleanPuppi.checkOverlaps.photons = cms.PSet()
cleanPuppi.checkOverlaps.taus = cms.PSet()
cleanPuppi.checkOverlaps.tkIsoElectrons = cms.PSet()
cleanPuppi.finalCut = ""#pt > 80"# & abs(eta) < 2.4"#pt > 20 & abs(eta) < 2.4"



fatPuppiSequence = cms.Sequence( goodPuppi + cleanPuppi )

