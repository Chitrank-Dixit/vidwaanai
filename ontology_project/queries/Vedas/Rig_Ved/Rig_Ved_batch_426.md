# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Rig Ved 0.8501)
- **Original**: भवा न: शुभ्र सातये
- **Translation**: 

---

### Verse 2 (Rig Ved 0.8502)
- **Original**: हे मनुष्यो ! आप ऊन के समान मृदु एवं सुखप्रद आसनों को बिछायें; क्योंकि स्तोताओं ने स्तुतियाँ आरम्भ कर दी हैं। हे शुभ अभ्निदेव ! स्तुतियों से वृद्धि को प्राप्त हुए आप हमें ऐश्वर्य प्रदान करने वाले हों
- **Translation**: 

---

### Verse 3 (Rig Ved 0.8503)
- **Original**: 3693. देबीद्द्गारो वि श्रयध्ब॑ सुप्रायणा न ऊतये । प्रप्र यज्ञं पृणीतन
- **Translation**: 

---

### Verse 4 (Rig Ved 0.8504)
- **Original**: मं0 5 सृ0 6 9 हे हटियो ! आप उत्तम गुणों वाली, दिव्य ट्वारों को खोलने वाली और श्रेष्ठ कर्म वाली है। आप हमारों रक्षा के निमित्त यज्ञ को परिपूर्ण करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.8505)
- **Original**: 3694. सुप्रतीके वयोवृधा यड्डी ऋतस्य मातरा
- **Translation**: 

---

### Verse 6 (Rig Ved 0.8506)
- **Original**: दोषामुषघासमीमहे
- **Translation**: 

---

### Verse 7 (Rig Ved 0.8507)
- **Original**: सुन्दर रूप वाली, आयु बढ़ाने वालो, महान्‌ कर्मों को सम्पन्न कराने वाली, यज्ञ कममों की निर्मात्री रात्रि और उषा देवियों की हम उत्तम स्तुति करते हैं
- **Translation**: 

---

### Verse 8 (Rig Ved 0.8508)
- **Original**: 3695, वातस्य पत्मन्नीढ्िता दैव्या होतारा मनुष:
- **Translation**: 

---

### Verse 9 (Rig Ved 0.8509)
- **Original**: इम॑ नो यज्ञमा गतम्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.8510)
- **Original**: है अग्नि और आदित्य रूप दिव्य होताओ ! आप दोनों हम मनुष्यों के इस यज्ञ में स्तुति से प्रेरित होकर वायु की गति से आयें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.8511)
- **Original**: 3696. इब्छा सरस्वती पही तिस्रो देवीमयोभुवः । बहिं: सीदन्त्वल्लिधः
- **Translation**: 

---

### Verse 12 (Rig Ved 0.8512)
- **Original**: इला, सरस्वती और मही (महान्‌ भारती) तीनों देवियाँ सुखकारक हैं । ये मार्ग में अबाधित होकर हमारे यज्ञ में अशविष्ठित हों
- **Translation**: 

---

### Verse 13 (Rig Ved 0.8513)
- **Original**: 3697. शिवस्त्वष्टरिहा गहि विभु: पोष उत त्मना । यज्ञेयज्ञे न उदव
- **Translation**: 

---

### Verse 14 (Rig Ved 0.8514)
- **Original**: हे त्वष्टादेव ! आप व्यापक सामर्थ्य-सम्पन्न और कल्याणकारी कर्म करने वाले हैं । आप हमारे यज्ञ में आगमन करें । हमारे प्रत्येक यज्ञ कर्म के उत्तम पद में प्रतिष्ठित होकर हमारे रक्षक हों
- **Translation**: 

---

### Verse 15 (Rig Ved 0.8515)
- **Original**: 3698. यत्र वेत्थ वनस्पते देवानां गुह्या नामानि। तत्र ह॒व्यानि गामय
- **Translation**: 

---

### Verse 16 (Rig Ved 0.8516)
- **Original**: हे वनस्पते ! जहाँ-जहाँ आप देवों के गुप्त स्थानों को जानते हैं, वहाँ-वहाँ इन हव्यादि साधनों को पहुँचायें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.8517)
- **Original**: 3699. स्वाहाग्नये वरुणाय स्वाहेन्द्राय मरुद्भ्य: । स्वाहा देवेभ्यो हवि:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.8518)
- **Original**: यह हवि अग्नि और वरुण देवों के लिए समर्पित है । यह हवि इद्धदेव और मरुदगणों के लिए समर्पित है
- **Translation**: 

---

### Verse 19 (Rig Ved 0.8519)
- **Original**: [सूक्त- 6 ] [ ऋषि - वसुश्रुत आत्रेय
- **Translation**: 

---

### Verse 20 (Rig Ved 0.8520)
- **Original**: देवता - अग्ति । छत्द - पंक्ति
- **Translation**: 

---

