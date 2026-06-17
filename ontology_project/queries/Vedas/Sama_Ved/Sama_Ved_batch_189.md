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

### Verse 1 (Sama Ved 0.3761)
- **Original**: 1473. शुष्मी शर्धो न मारुतं पवस्वानभिशस्ता दिव्या यथा विदू । आपो न मक्षू सुमतिर्भवा न: सहस्नाप्सा: पृतनाषाण्न यज्ञ:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3762)
- **Original**: हे सोमदेव ! मरुदगणों के तुल्य बल प्राप्त करने के लिए आप पवित्र हों । जैसे दिव्य प्रजा परस्पर ईर्ष्या निन्‍्दासे दूर अखण्ड रहती है , वैसे ही आप जल के समान पवित्र होकर हमारे लिए उत्तम बुद्धि प्रदान करें । अनेक रूपों में विभूषित, शत्रुविजेता आप यज्ञ के सदृश पूज्य हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3763)
- **Original**: 1474. त्वमग्ने यज्ञानां होता विश्वेषं हितः। देवेभिर्मानुषे जने
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3764)
- **Original**: है अग्निदेव ! आप सब यज्ञों को सम्पन्न करने वाले हैं। देवताओं ने आपको मानव-मरात्र के कल्याण के लिए नियुक्त किया है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3765)
- **Original**: 9475. स नो मन्धराभिरध्वरे जिह्नाभिर्यजा मह:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3766)
- **Original**: आ देवान्वक्षि यक्षि च
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3767)
- **Original**: है अग्निदेव ! आप हमारे यज्ञ में हर्षवर्द्धक ज्वालाओं के द्वारा देवों का यजन करें । देवताओं का आबाहन कर उन्हें तृप्तिदायक हविष्यानन अर्पित करें
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3768)
- **Original**: 13.6 सापवेद-संहिता 1476. वेत्था हि वेधो अध्वन: पथश्च देवाज्लसा। अग्ने यज्ञेषु सुक्रतो
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3769)
- **Original**: हे नियन्ता, श्रेष्ठकर्मा अग्ने ! आप यज्ञ के निकटस्थ एवं दूरस्थ सभी मार्गों के ज्ञाता हैं। आप याजकों का उचित मार्गदर्शन करें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3770)
- **Original**: 1477. होता देवो अमर्त्य: पुरस्तादेति मायया
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3771)
- **Original**: विदथानि प्रचोदयन्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3772)
- **Original**: यज्ञ करने वाले, अविनाशी, प्रकाशमान अग्निदेव, याजकों (साधकों ) को सत्कर्म की प्रेरणा देते हुए शीघ्र ही प्रकट होते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3773)
- **Original**: 1478. बाजी बाजेषु धीयते5ध्वेरेषु प्र णीयते । विप्रो यज्ञस्थ साधन:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3774)
- **Original**: संग्राम में बलशाली अग्निदेव को शत्रु-नाश करने के निमित्त स्थापित करते हैं। ये ज्ञानसम्पन अग्निदेव यज्ञ-कर्मों को सिद्ध करने वाले साधनरूप हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3775)
- **Original**: 1479. धिया चक्रे वरेण्यो भूतानां गर्भमा दथे । दक्षस्थ पितरं तना
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3776)
- **Original**: वे अग्निदेव सब यज्ञ-कर्मों में प्रकट होने के कारण श्रेष्ठ हैं। सब प्राणियों में संव्याप्त हैं । विश्वपालक अस्निदेव को दक्ष-पुत्री (वेदी-स्वरूपिणी) यज्ञादि के निमित्त धारण करती हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3777)
- **Original**: इति पंचम: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3778)
- **Original**: षष्ठ: खण्ड:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3779)
- **Original**: 1480. आ सुते सिद्धत श्रियं रोदस्योरभिश्रियम्‌। रसा दधीत वृषभम्‌
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3780)
- **Original**: हे अध्वर्युगण ! आकाश और पृथ्वी में देदीप्यमान दुग्ध (घवल किरणों) से सोम का मिश्रण करो । (क्योंकि) बाद में वह दुग्ध (धवल तेज) बलशाली.सोम को आत्मसात्‌ कर लेता है । (और स्वयं अत्यधिक बलशाली बन जाता है ।)
- **Translation**: 

---

