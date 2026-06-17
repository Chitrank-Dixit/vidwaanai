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

### Verse 1 (Vishnu Puran 0.9941)
- **Original**: जम्भके मरनेपर जैसे देवताओने इन्द्रकों स्तुति की थी उसो प्रकार अरिशसुरके जम्भे हते सहस्राक्ष पुरा देवगणा यथा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9942)
- **Original**: मस्तेपर गोपगण श्रीजनार्दनकी प्रशंसा करने कगे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9943)
- **Original**: नस जब लत इति श्रीविष्णुपुराणे पह्ममें5ो चतुर्दशोउध्यायः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9944)
- **Original**: ं_--» जौ 00000»
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9945)
- **Original**: आ 175) पक्षम अंश पन्द्रहवाँ अध्याय कंसका श्रीकृष्णको बुल्ानेके लिये अक्रूरकों भेजना औीपराजर उवाच ककुदाति हतेउरिप्टे धेनुके बिनिपातिते। प्रलृम्बे निधन नीते धृते गोवर्धनाचले। 91 दमिते कालिये नागे भश्ने तुदद्मपइये। हतायां पूतनायां ज् शंकटे परिवर्तिते
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9946)
- **Original**: 2 कंसाय नारदः प्राह यथावृत्तमनुक्रमात्‌ । “3
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9947)
- **Original**: 3 श्रुत्वा तत्सकल्ं कंसो नारदाहेेवरदर्शनात्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9948)
- **Original**: बसुदेव॑ प्रति तदा कोप चक्रे सुदुर्मीति:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9949)
- **Original**: कंसने सो$तिकोपादुपालभ्य सर्वयादवसंसदि । जग यादवांज्षैव कार्य चैतदचिन्तयत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9950)
- **Original**: 5 यावत्र बलमारूढो रामकृष्णो सुबालको । ताबदेब मया वध्यावसाध्यों रूढयोबनौ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9951)
- **Original**: 6 चाणूरोउत्र महावीयों मुप्टिकश्ष महाबल: । एताभ्यां मल्लयुद्धेन मारयिष्यामि दुर्मती
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9952)
- **Original**: 7 धनुर्महमहायोगव्याजेनानीय तौ बव्रजात्‌ । तथा तंथा यतिष्यामि यास्येते सद्भयं यथा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9953)
- **Original**: 8 घातयिष्यति वा गोपौ वसुदेवसुतावुभौ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9954)
- **Original**: 19 अपयाशर ठवाच इत्यालोच्य स दुष्टात्मा कंसो रामजनार्दनों । हन्तुं कृतमतिर्वीरावक़ूरं वाक्यमग्रवीत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9955)
- **Original**: 12 श्रीपराशरजी खोले--त॒पभरूपथारी अरिष्टासुर, थेनुक और भ्ररूम्ब आदिका वध, गोवर्धनपर्वतका घारण करना, काल््यिनागका दमन, दो विशाल वृक्षोका उखाड़ना, पूतनावध तथा शकटका उल्डट देना आदि अनेक लौल्मएँ हो जानेपर एक दिन नारदजीने कंसको, यद्ोदा और देवकीके गर्भ-परिवर्तनसे लेकर जैसा-जैसा हुआ था, वह सब यृत्तान्त क्रमशः सुना दिया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9956)
- **Original**: देखदर्दान नारदजीसे ये सब बातें सुनकर दुर्बुद्ध बसुदेवजीके प्रति अत्यत्त क्रोध प्रकट किया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9957)
- **Original**: उसने अत्यन्त क्प्रेपसे वसुदेवजीको सम्पूर्ण यादलॉकी सभामें डॉटा तथा समस्त यादवोंकी भी निन्‍्दा की और यह कार्य विचारने छगा--“ये अत्यन्त बालक राम और कृष्ण ज्बतक पूर्ण बल प्राप्त नहीं करते हैं तभीतक मुझे इन्हें मार देना चाहिये, क्योंकि युवावस्था प्राप्त होनेपर तो ये अजेय हो जायैंगे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9958)
- **Original**: मेरे यहाँ महावीर्यशाली चाणूर और महाबली मुष्टिक-जैसे मलल हैं। मैं इनके साथ मल्लयुद्ध कराकर उन दोनों दुर्बुद्धियॉंको मरवा डालँंगा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9959)
- **Original**: उन्हें महान्‌ धनुर्यज्ञके मिससे ब्रजसे बुलाकर ऐसे-पऐसे उपाय करूँगा जिससे के नष्ट हो जायैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9960)
- **Original**: उन्हें व्यनेके लिये मैं ँ्रफल्कके पुत्र यादबश्रेष्ठ शूरबीर अक्रूरको गोकुल भेजूँगा
- **Translation**: 

---

