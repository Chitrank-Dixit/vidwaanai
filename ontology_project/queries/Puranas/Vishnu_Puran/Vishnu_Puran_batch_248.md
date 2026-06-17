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

### Verse 1 (Vishnu Puran 0.4941)
- **Original**: 27 एबमुक्तो ददौ तस्मै यजूंषि भगवात्रविः। अयातयापसंज़ानि यानि वेत्ति न तद्ुरु:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4942)
- **Original**: 28 यजूंषि ग्रैरधीतानि तानि विष्रैद्विजोत्तम । बाजिनस्ते सम्राख्याता: सूयोंउप्यश्रो3भवक्‍द्यात:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4943)
- **Original**: 29 शाखाभेदास्तु तेषां तै दशा पञ्च च वाजिनाम_। काण्वाद्यास्मुमहाभाग याज्ञवल्क्या: प्रकीर्तिता:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4944)
- **Original**: 30 . हे जिनके किरण-समूहका स्पर्श होनेपर लोक कर्मानृष्ठानके योग्य होता है, उन पत्ित्रताके कारण, शुद्धस्वरूप सूर्यदेशको नमस्कार है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4945)
- **Original**: 23 । भगवान्‌ सबिता, सूर्य, भास्कर और बिवस्वान॒कों नमस्कार है, देखता आदि समस्त भूतोकि आदिभूत आदित्यदेजयको आरम्यार नमस्कार है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4946)
- **Original**: जिनका तेजोमय रथ है, [अज्ञारूप] ध्वजाएँ हैं, जिन्हें (छत्दोमय] अमर अश्वगण यहन करते हैं तथा जो ब्रिभुवनकों प्रकाशित करनेवाले नेत्ररूप हैं, उन सूर्यदेवको मैं नमस्कार करता हूँ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4947)
- **Original**: अीपराशरजी बोले--उतके इस प्रकार स्तुति करनेपर भगयान्‌ सूर्य अश्ररूपसे प्रकट होकर जोछे---'त्‌म अपना अभीष्ट वर माँगो'
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4948)
- **Original**: तब याज्ञवल्क्यजीने उन्हें प्रणाम करके कहा--'आप मुझे उन यजुःश्रुतियोंका उपदेश कीजिये उिन्हें मेंरे गुरूजो मो न जानते हों”
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4949)
- **Original**: उनके ऐसा कहनेपर भगलान्‌ सूर्यने उन्हें अयातयाम नामक यजु: श्वुतियोंका उपदेदा दिया जिन्हें उनके गुरु वैज्ञम्पायनजी भो नहों जानते थे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4950)
- **Original**: हे द्विजोत्तम ! उन श्रुतियोंको जिन ब्राह्मणोंने पढ़ा था बे बाजी-नामसे निरूयात हुए क्योंकि उनका उपदेश करते समय सूर्य भी अश्वरूप हो गये थे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4951)
- **Original**: है महाभाग ! उन वाजिश्रुतियोंकी काण्व आदि पन्द्रह शाख्थाएँ हैं; जे सब झासाएँ महर्षि याज्ञवल्क्यकी प्रवृत्त की हुई कही जाती हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4952)
- **Original**: इति श्रीविष्णुपुराणे तृतीयेंडशो पम्रमोउध्याय:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4953)
- **Original**: कतज+ ++-+ ह# $ ननसित-ः छठा अध्याय सामवेदकी शाखा, अठारह पुराण और चौदह विद्याओंके विभागका वर्णन सामवेदतरोइशाखा व्यासशिष्यस्स जैमिनि: । क्रमेण येन मैत्रेय बिभ्ेद श्रृूणु तत्मम
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4954)
- **Original**: 91 पुत्रो5भूत्सुकर्मास्थाप्यभूत्सुत: । अधीतवन्तो चैकैकां संहितां तो महामती
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4955)
- **Original**: 2 सहसखसंहिताभेदं ः चकार तं अक असहा महाव्तो
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4956)
- **Original**: 3 उदीच्यास्सामगा: शिष्यास्तस्य पश्नझत स्मृता:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4957)
- **Original**: श्रीपराहरजी जोले--हे मैत्रेय ! जिस क्रमसे व्यासजीके दिल्य जैमिनिने सामवेदकी झ्ञाख्ाओंका विभाग किया था, वह मुझसे सुनो
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4958)
- **Original**: जैमिनिका पुत्र सुमन्तु था और उसका पुत्र सुकर्मा हुआ। उन दोनों सहासति पुत्र-पौजोंने सामवेदकी एक-एक दझाख्ताका अध्ययन क्रिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4959)
- **Original**: तदनन्तर सुमन्तुके पुत्र सुकर्माने हे ट्विजोत्तम ! उन्हें उसके कौसल्य हिरण्यनाभ तथा पौष्पिज्ञि नामक दो महात्रती शिष्योने ग्रहण किया। हिरण्यनाभके पाँच सौ दिष्य थे जो उदीच्य सामग 3
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4960)
- **Original**: कहलाये
- **Translation**: 

---

