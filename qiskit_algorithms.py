from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
from qiskit.algorithms import Grover, AmplificationProblem, VQE
from qiskit.circuit.library import EfficientSU2, MCMT, ZGate
from qiskit.algorithms.optimizers import COBYLA
from qiskit.opflow import PauliSumOp
from qiskit.utils import algorithm_globals
import numpy as np

# 1. Bell State Creation
def bell_state():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    return qc

# 2. Grover's Algorithm (Search for |11> in 2-qubit space)
def grovers_algorithm():
    oracle = QuantumCircuit(2)
    oracle.cz(0, 1)
    problem = AmplificationProblem(oracle)
    grover = Grover()
    result = grover.amplify(problem)
    return result.circuit

# 3. Quantum Teleportation
def quantum_teleportation():
    qc = QuantumCircuit(3, 1)
    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)
    qc.measure(0, 0)
    qc.cx(1, 2)
    qc.cz(0, 2)
    return qc

# 4. Shor’s Algorithm (Factoring 15 - Basic Simulation)
def shors_algorithm():
    from qiskit.algorithms import Shor
    backend = Aer.get_backend("qasm_simulator")
    shor = Shor()
    result = shor.factor(N=15)
    return result

# 5. Variational Quantum Eigensolver (VQE)
def vqe_solver():
    algorithm_globals.random_seed = 42
    operator = PauliSumOp.from_list([("Z", -1.0), ("X", 0.5)])
    ansatz = EfficientSU2(1)
    optimizer = COBYLA(maxiter=100)
    vqe = VQE(ansatz, optimizer, quantum_instance=Aer.get_backend("statevector_simulator"))
    result = vqe.compute_minimum_eigenvalue(operator)
    return result

# 6. Quantum Tunneling Simulation
def quantum_tunneling():
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Put the qubit in superposition
    qc.barrier()
    qc.measure(0, 0)  # Simulate measuring whether the particle tunneled
    return qc

if __name__ == "__main__":
    backend = Aer.get_backend("qasm_simulator")
    
    print("\n--- Bell State Execution ---")
    bell_circuit = bell_state()
    result = execute(bell_circuit, backend, shots=1024).result()
    print(result.get_counts())
    
    print("\n--- Grover's Algorithm Execution ---")
    grover_circuit = grovers_algorithm()
    result = execute(grover_circuit, backend, shots=1024).result()
    print(result.get_counts())
    
    print("\n--- Quantum Teleportation Execution ---")
    teleport_circuit = quantum_teleportation()
    print(teleport_circuit.draw())
    
    print("\n--- Shor’s Algorithm Execution ---")
    shor_result = shors_algorithm()
    print(shor_result)
    
    print("\n--- VQE Execution ---")
    vqe_result = vqe_solver()
    print(vqe_result)
    
    print("\n--- Quantum Tunneling Execution ---")
    tunneling_circuit = quantum_tunneling()
    result = execute(tunneling_circuit, backend, shots=1024).result()
    print(result.get_counts())
