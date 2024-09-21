// Returns a random DNA base
const returnRandBase = () => {
    const dnaBases = ['A', 'T', 'C', 'G']
    return dnaBases[Math.floor(Math.random() * 4)] 
  }
  
  // Returns a random single strand of DNA containing 15 bases
  const mockUpStrand = () => {
    const newStrand = []
    for (let i = 0; i < 15; i++) {
      newStrand.push(returnRandBase())
    }
    return newStrand
  }

  function pAequorFactory(number, bases) {
    return {
        _specimenNum: number,
        _dna: bases,
        mutate() {
            randomBase = Math.floor(Math.random() * 15);
            dnaBasesNoA = ['T', 'C', 'G'];
            dnaBasesNoT = ['A', 'C', 'G'];
            dnaBasesNoC = ['A', 'T', 'G'];
            dnaBasesNoG = ['A', 'T', 'C'];
            if (this._dna[randomBase] === 'A') {
                this._dna[randomBase] = dnaBasesNoA[Math.floor(Math.random() * 3)];
              } else if (this._dna[randomBase] === 'T') {
                this._dna[randomBase] = dnaBasesNoT[Math.floor(Math.random() * 3)];
              } else if (this.dna[randomBase] === 'C') {
                this._dna[randomBase] = dnaBasesNoC[Math.floor(Math.random() * 3)];
              } else {
                this._dna[randomBase] = dnaBasesNoG[Math.floor(Math.random() * 3)];
              }
              return this._dna;
        },
        compareDNA(pAequor) {
            numberCommon = 0;
            //numberCommonality = 0;
            for (let i = 0; i < pAequor['dna'].length; i++) {
                if (pAequor.dna[i] === this._dna[i]) {
                    numberCommon++;
                }
            }
            percentCommon = ((numberCommon / 15) * 100).toFixed(2);
            console.log(`Specimen #${this._specimenNum} and Specimen #${pAequor._specimenNum} have ${percentCommon}% DNA in common.`)
        },
        willLikelySurvive() {
            cAndGCounter = 0;
            for (let i = 0; i < this._dna.length; i++) {
              if (this._dna[i] === 'C' || this._dna[i] === 'G') {
                cAndGCounter++;
              }
            }
            if (cAndGCounter < 9) {
              return false;
            } else {
              return true;
            }
          }
        };
      };
      
      // Creating 30 pAequor that are likely to survive
      const survivors = [];
      while (survivors.length < 30) {
        pAequorNumber = survivors.length + 1;
        newPAequor = pAequorFactory(pAequorNumber, mockUpStrand());
        if (newPAequor.willLikelySurvive() === true) {
          survivors.push(newPAequor);
        }
      }
      console.log(survivors);
