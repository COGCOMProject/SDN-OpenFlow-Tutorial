from pox.core import core
import pox.openflow.libopenflow_01 as of

from pox.lib.util import dpidToStr
log = core.getLogger()


def _handle_PacketIn (event):
	packet = event.parsed
	
	if event.port == 2:
		msg = of.ofp_flow_mod()
		msg.connection = event.connection
		msg.match.in_port = event.port
		msg.hard_timeout = 30
		msg.match.dl_src = packet.src
		msg.match.dl_dst = packet.dst
		msg.actions.append(of.ofp_action_output(port = 4))
		event.connection.send(msg)
		print "Sending massage in port = ", event.port
	elif event.port == 4:
		msg = of.ofp_flow_mod()
		msg.connection = event.connection
		msg.match.in_port = event.port
		msg.hard_timeout = 30
		msg.match.dl_src = packet.src
		msg.match.dl_dst = packet.dst
		msg.actions.append(of.ofp_action_output(port = 2))
		event.connection.send(msg)	
		print "Sending massage in port = ", event.port
	else:
		msg = of.ofp_flow_mod()
		msg.connection = event.connection
		msg.match.in_port = event.port
		msg.hard_timeout = 15
		msg.match.dl_src = packet.src
		msg.match.dl_dst = packet.dst
		event.connection.send(msg)	
		print "Dropping massage in port = ", event.port	
	
	
def launch ():
	print ""
	print "------------------------------------------"
	print "|        SDN / Openflows Tutorial        |"
	print "------------------------------------------"
	print ""
	core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
