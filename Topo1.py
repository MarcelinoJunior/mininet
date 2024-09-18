#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def simpleNetwork():
    """
    Cria uma rede simples com dois hosts e um switch.
    """
    # Cria a rede
    net = Mininet(controller=Controller)

    info('*** Criando Controlador \n')
    net.addController('c0')

    info('*** Criando hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')

    info('*** Criando switch\n')
    s1 = net.addSwitch('s1')

    info('*** Criando links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    info('*** Iniciando o Laboratorio\n')
    net.start()

    info('*** Teste de conectividade\n')
    net.pingAll()

    info('*** Liberando CLI\n')
    CLI(net)

    info('*** Encerrando Laboratorio\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')  # Defina o nivel de log para 'info' para ver as mensagens de log.
    simpleNetwork()
