import logging

logger = logging.getLogger(__name__)

# TODO: create_abstract_nsubj

def copy_features(node):
	if node.get("feats"):
		for feat in node["feats"]:
			node["ms feats"][feat].add(node["feats"][feat])
	else:
		logger.warning("Node %s has no features", node)