def switch_case(token, parent = None):
	lemma = token["lemma"]
	deprel = token["deprel"]

	#======<Static location>===========================================
	# Inessive
	if lemma in ["in", "entro", "dentro"]:
		return "Ine"
	
	# NOTE: 'entro' has also many occurrences in which it is temporal Lim (e.g., 'entro sessanta giorni dalla consegna dalla pubblicazione della legge', ISDT), however, promoted spatial sense, according to the guidelines.

	# Interessive
	# TODO: decide how to treat things that are not 'fixed' e.g., 'in mezzo a', which could be mapped to 'Ces' (Interessive)
	
	# Intrative (between X and Y)
	if lemma in ["tra", "fra"]:
		return "Int"

	# External
	if lemma in ["fuori", "fuori da"]:
		return "Ext"

	# Superadessive
	if lemma in ["su", "su di"]:
		return "Adt"
	
	# NOTE: 'su di' can also have a The - Themative meaning: 'i libri che si scriveranno su di lui' 'the books that will be written about him'.

	# Apudessive (next to something)
	if lemma in ["accanto a"]:
		return "Apu"

	# Circumessive
	if lemma in ["attorno a", "intorno a"]:
		return "Cir"
	
	# Proximative
	if lemma in ["vicino", "vicino a"]:
		return "Prx"
	
	# Distantive
	if lemma in ["lontano da"]:
		return "distantive"
	
	# Superessive
	if lemma in ["sopra"]:
		return "Sup"
	
	# Subessive
	if lemma in ["sotto"]:
		return "Sub"
	
	# TODO: handle 'sopra o sotto'
	
	# Antessive
	if lemma in ["davanti", "davanti a"]:
		return "Ant"

	# Postessive
	if lemma in ["dietro", "dietro a", "dietro di"]:
		return "Pst"

	# Oppositive
	# TODO: decide how to treat things that are not 'fixed' e.g., 'di fronte a', which could be mapped to 'Opp' (Oppositive)
	#======<\Static location>============================================

	#======<Direction focused on origin>=================================
	
	# Ablative
	if lemma in ["da"]:
		if parent["deprel"] != "obl:agent":
			return "Abl"

	# TODO: avoid falling back to default when deprel == obl:agent

	#======<\Direction focused on origin>==================================
	
	#======<Direction focused on path>=====================================

	# Perlative
	if lemma in ["tramite"]:
		return "Per"
	
	# TODO: decide on 'per mezzo di'
	# TODO: decide between Perlative and Instrumental
	
	# Perlative across
	if lemma in ["attraverso"]:
		return "Crs"
	
	# Perlative along
	if lemma in ["lungo"]:
		return "Lng"
	
	# Prolative
	if lemma in ["via"]:
		return "Pro"
	# NOTE: es. 'via fax'

	# Ascentive: deprel = advmod 'su' ?
	# Descentive: deprel = advmod 'giù' ?

	#======<\Direction focused on path>====================================
	
	#======<Direction focused on destination>==============================
	
	# Lative
	if lemma in ["a", "verso"]:
		if deprel == "case":
			return "Lat"
		elif deprel == "mark":
			return "Pur"
	
	# NOTE: it seems impossible to distinguish when "a" introduces a Dative. It it. treebanks when the indirect object is realized as a prepositional phrase, it is labeled as obl (ex. Dare a qualcuno qualcosa, give something to someone).

	# NOTE: 'verso' can be also temporal approximative
	
	#======<\Direction focused on destination>==============================

	#======<Temporal>=======================================================
	
	# Temporal antessive
	if lemma in ["prima di", "prima che"]:
			return "Tan"
	
	# Temporal postessive (after a point or period)
	if token["lemma"] in ["dopo", "dopodiché", "dopo di che"]:
			return "Tps"

	# TODO: decide on 'in seguito (a)'

	# Temporal terminative
	if token["lemma"] in ["fino a", "finché", "fino a che"]:
			return "Ttr"
	
	# NOTE: it's normal that when deprel = mark the lemma has only temporal meaning and when deprel = case it can have both temporal and spatial, because if it is 'mark' then it's anchored to an 'event' and an 'event' cannot be before, after or until in a spatial sense, but only in a temporal sense. 

	# Temporal (at, on, in, upon a point in time)
	if token["lemma"] in ["appena", "quando", "allorché", "allorquando"]:
		return "Tem"
	
	# NOTE: 'Quando' (when) is also conditional, but we treat the conditional meaning as an extension of the temporal. 
	
	# Durative (during a period)
	if token["lemma"] in ["mentre"]:
		return "Dur"
	
	# deprel = advmod; frattanto, intanto (Durative - Dur).
	# deprel = advmod; circa (Temporal approximative - Tpx). But also not temporal (is approximative in general: circa il 12% della popolazione; no case of approximation beside temporal approximation).

	# TODO: decide on 'da allora' = temporal egressive
	#======<\Temporal>======================================================

	#======<Relation>=======================================================
	
	# Genitive
	if token["lemma"] in ["di"]: # be aware of polysemy
		return "Gen"
	
	# Comitative
	if token["lemma"] in ["con"]: # be aware of polisemy
		return "Com"

	# Abessive (without something)
	if token["lemma"] in ["salvo che", "senza", "senza che"]:
		return "Abe"
	
	# TODO: decide how to treat things that are not 'fixed': e.g., 'a meno che'.
	
	# NOTE: in 'inventory.md' also 'salvo' is under Absessive, but in the treebank 'salvo' has deprel = amod and is considered 'ADJ'.

	# Inclusive
	# TODO: decide what to do with form = 'compreso', 'incluso'.

	# Additive (besides, in addition to something)
	if token["lemma"] in ["oltre", "oltre a", "oltre che"]:
		return "Add"
	
	# NOTE: example: "... pagando, oltre il valore della metà del muro, il valore del suolo da occupare con la nuova fabbrica)". However, 'oltre' can also be used as a Spx (Superprolative) (or simply Superessive ?) ex. "In Italia vi sono oltre 40 modelli posti in commercio da una ventina di distributori". 

	# Exclusive
	if token["lemma"] in ["tranne", "tranne che", "tranne in", "eccetto", "eccetto che", "tranne quando", "fuorché"]:
		return "Exc"
	
	# NOTE: Exclusive - lemmas from LICO "Negative condition:Arg2" + "Exception:Arg2"

	# TODO: precise difference between Abessive and Exclusive?

	# Substitutive
	if token["lemma"] in ["anziché", "piuttosto che", "invece di"]:
		return "Sbs"

	# NOTE: Substitutive - lemmas from LICO Substitution:Arg1
	# deprel = advmod; 'piuttosto che' (Sbs - Substitutive)
	# TODO: decide what to do with 'al posto di' [lemma = 'posto', child lemma = 'a', 'il'], 'in luogo di'.

	#======<\Relation>======================================================

	#======<Similarity>=====================================================

	# Essive
	# TODO: decide on 'in qualità di'
	if lemma ["quale"]:
		return "Ess"

	# NOTE: in some cases it's ok to attribute 'quale' deprel = case, mark to essive. However, there are also cases in which it has an 'instantiation' (for-example) meaning: "Troppe persone lavorano in l'industria di i servizi tradizionali a bassa produttività, come il commercio a l'ingrosso e a il dettaglio e la ristorazione, lasciando in uno stato di arretratezza servizi moderni e ad alta produttività quali le comunicazioni, la salute, l'intermediazione finanziaria e i servizi aziendali."

	# For 'come' this 'instantiation' meaning is even more common and I would not feel comfortable in mapping 'come' as neither essive, nor equative nor semblative.

	# Equative
	if lemma ["così come"]:
		return "Equ"
	
	# Semblative (?)
	if lemma ["quasi"]:
		return "Sem" 
	
	# Example: Era il quarto d'ora di il secondo tempo iniziato in anticipo, quasi ci fosse la fretta di chiudere la pratica e che non ci si pensasse più.

	# Dissemblative
	# TODO: decide on 'a differenza di'

	# Comment ??? 


	#======<\Similarity>====================================================
	
	#======<Cause, consequence, circumstance, other>========================
	
	# Causative
	
	# NOTE: source: LICO Contingency:Cause:Reason (they're all hypotactic)

	if lemma in ["giacché", "perché", "perciò", "poiché", "siccome", "per", "grazie a", "in quanto"]:
		return "Caus"
	
	# TODO: 'a causa di' 
	# TODO: 'dato che' (fixed) (tree strano)
	# NOTE: 'per' is highly polisemic.
	# NOTE: perciò deprel = 'mark' (9 occ) vs. 'perciò' deprel = advmod (30 occ) - don't understand why different deprels. 

	# Purposive
	# TODO: work in progress
	# NOTE: source: LICO Contingency:Purpose

	if lemma in ["affinché", "pure di"]:
		return "Pur"
	
	# Considerative

	# TODO: find a place for 'rispetto a' (which is not considerative). 'Rispetto a' is like setting a baseline to which something is compared.

	# Ignorative

	# TODO: decide on 'a prescindere da'
	
	# Concessive
	# NOTE: source: LICO Comparison:Concession:Arg1

	# TODO: 'a dispetto di', 'per quanto' (?)

	if token["lemma"] in ["anche se", "ancorché", "benché", "comunque", "malgrado", "nonostante", "quantunque", "sebbene", "seppure"]:
		return "Ccs"  
	
	# lemma = seppur(e) in ISDT has only 2 occurrences and one time is deprel = mark and the other is deprel = advmod

	# lemma = "tuttavia", deprel = "advmod": concessive?
	# lemma = eppure, deprel = "advmod"; concessive?
	
	# Conditional
	# NOTE: source: LICO Contingency:Condition

	# TODO: 'a condizione che', 
	# TODO: Conj of values: 'se, come e quando'
	# TODO: Conj of values: 'solo e quando'

	if lemma in ["casomai", "purché", "qualora", "se", "sempreché", "solo"]:
		return "Cnd"
	
	# Themative

	# TODO: 'per quanto riguarda'
	if lemma in ["riguardo", "riguardo a", "circa"]:
		return "The"

	# Quotative
	if lemma in ["secondo"]:
		return "Quo"
	
	# Instrumental
	if lemma in ["mediante"]:
		return "Ins"
	
	# TODO: decide on the belonging of 'tramite' and 'per mezzo di' to Perlative. Aren't they more 'Ins'? Should we promote spatial senses?

	# Adversative
	if token["lemma"] in ["contro"]:
		return "Adv"
	
	# 'anti', suggested in 'inventory.md' is usually a prefix 'anti-'. When written with a whitespace in between is marked with deprel = amod and considered an ADJ.

	#======<\Cause, consequence, circumstance, other>=====================================================

	return f"TBD-'{token['lemma']}'"

def switch_conj_case(token):

	#======<\Coordination>=====================================================

	# Conjunctive
	if token["lemma"] in ["e", "ed"]:
		return "Conj"

	# Disjunctive
	if token["lemma"] in ["o", "oppure"]:
		return "Disj"

	#Negative disjunctive
	if token["lemma"] in ["né"]:
		return "Nnor"

	# Adversative
	if token["lemma"] in ["ma", "però", "bensì"]:
		return "Advs"
	
	# NOTE: many 'però' are deprel = advmod
	# TODO: decide on 'per contro', 'al contrario', 'invece' (deprel = advmod)

	if token["lemma"] in ["anziché", "piuttosto che"]:
		return "Sbs"
	# Here because in ISDT many 'anziché' and 'piuttosto che' have deprel = cc

	# Consequence
	# NOTE: source: LICO Contingency:Cause:Result
	# lemma = quindi, pertanto, dunque, così che, allora (?); deprel = advmod
	# NOTE: 'allora' has also other meanings: '... di cui era allora amministratore delegato Orsi' (true advmod?); 'da allora' (since) = temporal egressive. 
	# lemma = conseguenza; child = di/come (?)

	#======<\Coordination>=====================================================

	return f"TBD-CONJ-{token['lemma']}"


def switch_verb_modality(token):

	if token["lemma"] == "potere":
		return "Pot"

	if token["lemma"] == "volere":
		return "Des"

	if token["lemma"] == "dovere":
		return "Nec"

	# TODO: what about prms?


def switch_det_definitess(token):
	if token["lemma"] == "nessuno":
		return "Def"

	if token["lemma"] == "alcuno":
		return "Def"

	if token["lemma"] == "qualche":
		return "Ind"

	if token["lemma"] == "questo":
		return "Def"

	if token["lemma"] == "quello":
		return "Ind"

	# * accounts for dei, degli, della etc...
	if token["lemma"] == "di":
		return "Ind"


def switch_det_polarity(token):
	if token["lemma"] == "nessuno":
		return "Neg"

	if token["lemma"] == "alcuno":
		return "Neg"


def switch_det_dem(token):
	if token["lemma"] == "questo":
		return "Prox"

	if token["lemma"] == "quello":
		return "Dist"


# def switch_pron_person(token):
# 	if token["lemma"] in ["io", "noi", "mi", "ci"]:
# 		return "1"
# 	if token["lemma"] in ["tu", "voi", "ti", "vi"]:
# 		return "2"
# 	if token["lemma"] in ["lui", "lei", "egli", "ella", "esso", "essa",
# 								"loro", "le", "gli", "il", "lo", "la", "le", "li",
# 								"chi", "che", "si"]:
# 		return "3"
