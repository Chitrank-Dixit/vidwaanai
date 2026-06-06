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

### Verse 1 (Bramha 0.2421)
- **Original**: उत्कृष्ट स्बरूपका दर्शन किया, इससे मेरा सारा सब तुम्हारे सुखके उदय और कल्याणकी प्राप्तिका
- **Translation**: 

---

### Verse 2 (Bramha 0.2422)
- **Original**: मोह दूर हो गया। नाथ! अब मैं आपको कृपासे कारण है। तुमने लोकमें स्थावर-जज्मरूप जो
- **Translation**: 

---

### Verse 3 (Bramha 0.2423)
- **Original**: यह चाहता हूँ कि सम्पूर्ण लाकोंके हित, भिन्न- कुछ भी देखा है, वह सब सम्पूर्ण भूतोंकों उत्पन्न भिन्न भावनाओंकी पूर्ति तथा शैव और वैष्णवोंके करनेवाला मेरा आत्मा ही है, जिसे मैंने उस
- **Translation**: 

---

### Verse 4 (Bramha 0.2424)
- **Original**: विवाद-निवारणके लिये मैं इस परम उत्तम पतित्र रूपमें प्रकट किया है। मैं ही शड्ख, चक्र और
- **Translation**: 

---

### Verse 5 (Bramha 0.2425)
- **Original**: पुरुषोत्तमतीर्थमें भगवान्‌ शिवका बहुत बड़ा मन्दिर गदा धारण करनेवाला नारायण हूँ। जबतक एक
- **Translation**: 

---

### Verse 6 (Bramha 0.2426)
- **Original**: बनवाऊँ और उसमें शंकरजीको प्रतिष्ठा करूँ। हजार महायुगोंका समय नहीं बीत जाता, तबतक
- **Translation**: 

---

### Verse 7 (Bramha 0.2427)
- **Original**: इससे संसारके लोग यह जान लेंगे कि विष्णु और सम्पूर्ण बिश्वको मोहित करके यहाँ जलमें शयत
- **Translation**: 

---

### Verse 8 (Bramha 0.2428)
- **Original**: शिव एकरूप ही हैं।! यह सुनकर भगवान्‌ करता हूँ। मुनिश्रेष्! जबतक ब्रह्मा सोकर उठ
- **Translation**: 

---

### Verse 9 (Bramha 0.2429)
- **Original**: जगन्नाथने पुनः महामुनि मार्कण्डेयजीसे कहा-- नहीं जाते, तबतक मैं हर समय यहाँ शिशुरूपमें
- **Translation**: 

---

### Verse 10 (Bramha 0.2430)
- **Original**: 'ब्रह्मन्‌! तुम मेरी आज्ञासे शौघ्र ही एक मन्दिर निवास करता हूँ। विप्रेन्द! मुझ ब्रह्मरूपी परमात्माने
- **Translation**: 

---

### Verse 11 (Bramha 0.2431)
- **Original**: बनवाओ और उसमें नाना भाबोंकी पूर्ति एवं अनेक आर संतुष्ट होकर तुम्हें वरदान दिया है।
- **Translation**: 

---

### Verse 12 (Bramha 0.2432)
- **Original**: आराधनाके लिये परम कारणभूत भुवनेश्वर-लिब्ञकी समस्त चराचर जगत्‌का नाश होकर सब कुछ
- **Translation**: 

---

### Verse 13 (Bramha 0.2433)
- **Original**: स्थापना करो। उनके प्रभावसे तुम्हारा भगवान्‌ एकार्णवमें मग्र हो जानेपर तुम मेरी ही आज्ञासे
- **Translation**: 

---

### Verse 14 (Bramha 0.2434)
- **Original**: शिवके लोकमें अक्षय निवास होगा। शिवकी यहाँ आ निकले हो। फिर जब मेरे शरीरके भीतर स्थापना करनेपर मेरी हो स्थापना होती है। हम प्रविष्ट हुए हो तब मैंने तुम्हें सम्पूर्ण जगत्‌का
- **Translation**: 

---

### Verse 15 (Bramha 0.2435)
- **Original**: दोनोंमें तनिक भी अन्तर नहीं है। हम एक ही अवलोकन कराया है। वहाँ सम्पूर्ण लोकोंको
- **Translation**: 

---

### Verse 16 (Bramha 0.2436)
- **Original**: तत्त्व दो रूपमें व्यक्त हुए हैं। जो रुद्र हैं, वही देखकर तुम विस्मयमें पड़ गये और मुझे समझ
- **Translation**: 

---

### Verse 17 (Bramha 0.2437)
- **Original**: विष्णु हैं; जो विष्णु हैं बही महादेव हैं। वायु और नहीं पाये। तब तुरंत ही मैंने तुम्हें अपने मुखसे आकाशकी भाँति हम दोनोंमें कोई अन्तर नहीं बाहर निकाल दिया और जो देवता और असुरोंके
- **Translation**: 

---

### Verse 18 (Bramha 0.2438)
- **Original**: है। जो अज्ञानसे मोहित है, वह इस बातको नहीं लिये दुज्लेंय है, उस अपने आत्मतत्वका तुमसे
- **Translation**: 

---

### Verse 19 (Bramha 0.2439)
- **Original**: जानता कि जो गरुडध्यज हैं, वही यूषभध्वज हैं। वर्णन किया है। ब्रह्म! जबतक महातपस्व्री
- **Translation**: 

---

### Verse 20 (Bramha 0.2440)
- **Original**: अत: ब्रह्मन्‌! तुम अपने नामसे शिवालय बनवाओ
- **Translation**: 

---

