from pathlib import Path
import sys,unittest
sys.path.insert(0,str(Path(__file__).parents[1]/'tools'))
import execution_handoff as e
class T(unittest.TestCase):
    def test_dedup(self): self.assertEqual(len(e.reconcile_actions([{'work_id':'w','obligation_id':'o','cycle_id':'1'},{'work_id':'w','obligation_id':'o','cycle_id':'1'}])),1)
if __name__=='__main__': unittest.main()
