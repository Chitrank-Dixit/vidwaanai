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

### Verse 1 (Sama Ved 0.4541)
- **Original**: हे सूर्यदेव ! आप महान्‌ हैं । हे आलोककर्त्ता आप सचमुच महान हैं । हे स्तुतियोग्य
- **Translation**: 

---

### Verse 2 (Sama Ved 0.4542)
- **Original**: ! आपकी महिमा की हम स्तुति करते हैं । आपका व्यापक महत्व (प्रभाव) निश्वय हो आपको महान्‌ सिद्ध कर देता है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.4543)
- **Original**: 1789, बट सूर्य श्रवसा महाँ असि सत्रा देव महाँ असि । मह्ना देवानामसुर्य: पुरोहितो विभु ज्योतिरदाभ्यम्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.4544)
- **Original**: है सूर्यदेव ! आप अपने यश के कारण महान्‌ हैं । देवों के बोच विशेष महत्त्व के कारण आप महान्‌ हैं। आप तमिस्र (अन्धकार) रूपी असुरों का नाश करने वाले हैं, अत: पुरोहित के समान देवों का नेतृत्त्व करने वाले हैं । आपका तेज अदम्य, सर्वव्यापी और अविनाशो है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.4545)
- **Original**: इति द्वितीय:खण्डः
- **Translation**: 

---

### Verse 6 (Sama Ved 0.4546)
- **Original**: कु के के
- **Translation**: 

---

### Verse 7 (Sama Ved 0.4547)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.4548)
- **Original**: 1790. उप नो हरिभि: सुतं याहि मदानां पते । उप नो हरिभि: सुतम्‌
- **Translation**: 

---

### Verse 9 (Sama Ved 0.4549)
- **Original**: हे सोम के स्वामी इन्धदेव ! आप घोड़ों के द्वारा हमारे सोमयज्ञ में सोमपान के निमित्त अवश्यमेव पधारें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.4550)
- **Original**: 1791. द्विता यो बृत्रहन्तमो विद इन्द्र: शतक्रतु: । उप नो हरिभि: सुतम्‌
- **Translation**: 

---

### Verse 11 (Sama Ved 0.4551)
- **Original**: शत्रुनाशक और असंख्यकर्मा इन्रदेव, (शत्रुओं के नाश के साथ उग्र और आयों के रक्षण के समय शान्त) इन दो रूपों वाले हैं । वे हमारे द्वारा शुद्ध हुए सोम का पान करने घोड़ों से यहाँ आएँ
- **Translation**: 

---

### Verse 12 (Sama Ved 0.4552)
- **Original**: 1792. त्वं हि वृत्रहन्नेषां पाता सोमानामसि । उप नो हरिभि: सुतम्‌
- **Translation**: 

---

### Verse 13 (Sama Ved 0.4553)
- **Original**: हे दुष्ट-हन्ता इन्द्रदेव ! सोम को पीने के अभिच्छु आप हमारे यज्ञ में अश्वों के माध्यम से सोमपान के निमित्त पधारें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.4554)
- **Original**: 1793. प्र वो महे महेवृथे भरध्व॑ प्रचेतसे प्र सुमति कृणुध्वम्‌ । विशः पूर्वी: प्र चर चर्षणिप्रा:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.4555)
- **Original**: हे मनुष्यो ! अपने धन वृद्धि के लिए महान्‌ इद्धदेव को सोम अर्पित करो । इद्धदेव के निमित्त उत्तम स्तोत्रों का पाठ करो । हे प्रजापोषक इन्द्रदेव ! आप इन हवि दाताओं के समीप आएँ
- **Translation**: 

---

### Verse 16 (Sama Ved 0.4556)
- **Original**: 1794. उरुव्यचसे महिने सुवृक्तिमिन्द्राय ब्रह्म जनयन्त विप्रा: । तस्य ब्रतानि न मिनन्ति घीरा:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.4557)
- **Original**: अत्यन्त विशाल इन महान्‌ इन्द्रदेव को क्र््रत्वग्गण उत्तम स्तुतियाँ और हविष्यान्न अर्पण करते हैं । धीर पुरुष उन इन्द्रदेव के व्रतों को डिगाते नहीं हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.4558)
- **Original**: 1795, इन्द्र वाणीरनुत्तमन्युमेव सत्रा राजान॑ दधिरे सहध्यै । हर्यश्वाय बरहया समापीन्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.4559)
- **Original**: उत्तगर्चिके विशो5 ध्यायः 20.5 सबके राजा रूप इन्द्रदेव जिनके मन्यु (अनीति के प्रति क्रोध के आगे कोई टिक नहीं सकता) के प्रति की गयी स्तुतियाँ उनके शत्रु के पराभव का कारण बनती हैं । अत: हे स्तोताओ ! अपने स्वजनों को इन्द्रदेव की स्तुति की प्रेरणा दें
- **Translation**: 

---

### Verse 20 (Sama Ved 0.4560)
- **Original**: 1796, यदिन्द् यावतस्त्वमेतावदहमीशीय । स्तोतारमिद्रधिषे रदावसो न पापत्वाय रंसिषम्‌
- **Translation**: 

---

