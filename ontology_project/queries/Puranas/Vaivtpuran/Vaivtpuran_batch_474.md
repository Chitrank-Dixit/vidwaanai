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

### Verse 1 (Vaivtpuran 24.7049)
- **Original**: बलपूर्वक गौकों लानेके लिये नौकरोंको भेजा। उनसे विनयपूर्ण बचन कहा। इधर शोकके कारण, जिनका विवेक नष्ट हो गया राजा बोला--भक्तोंपर अनुग्रह करनेके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 24.7050)
- **Original**: था, वे मुनिवर जमदग्नि कपिलाके संनिकट जाकर लिये उद्यत रहनेवाले भक्तेश! आप तो कल्पतरुके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 24.7051)
- **Original**: रोने लगे और उन्होंने सारा वृत्तान्त कह सुनाया। समान हैं; अतः मुझ भक्तकों कामनापूर्ण करने-
- **Translation**: 

---

### Verse 4 (Vaivtpuran 24.7052)
- **Original**: तब भक्तोंपर अनुग्रह करनेके लिये उद्यत वाली इस कामधेनुको भिक्षारूपमें प्रदान कौजिये।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 24.7053)
- **Original**: रहनेबाली वह गौ, जो साक्षात्‌ लक्ष्मीस्वरूपा थी, तपोधन! आप-जैसे दाताओंके लिये भारतमें ब्राह्मणकों रोते देखकर बोली। * सा विद्या ततपों ज्ञानं स गुरु:स च बान्धव: । सा माता स पिता पुत्रस्तत्‌ क्षयं कारयेत्‌ तु यः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 24.7054)
- **Original**: (गणपतिखण्ड 24। 35)
- **Translation**: 

---

### Verse 7 (Vaivtpuran 24.7055)
- **Original**: * गणपतिखण्ड « 343 454444## 44444 44544 44% 444 4 % 44% कक कक कक 4 क4#ऋ कक कक 54 हक कक ऋ 5 कक कद कक 5 अक #8 888 88 सुरभिने कहा--मुने! जो निरन्तर अपनी इतना कहकर कामधेनुने सूर्यके सदृश वस्तुओंका शासक, पालक और दाता है, चाहे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 24.7056)
- **Original**: कान्तिमान्‌ नाना प्रकारके शस्सत्रास्त्र. और सेनाएँ वह इन्द्र हो अथवा हलवाहा, बही अपनी वस्तुका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 24.7057)
- **Original**: उत्पन्न कीं। उस कपिलाके मुख आदि अड्लोंसे दान कर सकता है। तपोधन! यदि आप
- **Translation**: 

---

### Verse 10 (Vaivtpuran 24.7058)
- **Original**: करोड़ों-करोड़ों खड्गधारी, शूलधारी, धनुर्धारी, स्वेच्छानुसार मुझे राजाको देंगे, तभी मैं स्वेच्छासे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 24.7059)
- **Original**: दण्ड, शक्ति और गदाधारी शूरवीर निकल आये। अथवा आपकी आज्ञासे उसके साथ जाऊँगी।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 24.7060)
- **Original**: करोड़ों वीर राजकुमार और म्लेच्छ निकले। इस यदि आप नहीं देंगे तो मैं आपके घरसे नहीं
- **Translation**: 

---

### Verse 13 (Vaivtpuran 24.7061)
- **Original**: प्रकार कपिलाने मुनिको सेनाएँ देकर उन्हें निर्भय जाऊँगी। आप मेरे द्वारा दी गयी सेनाके सहारे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 24.7062)
- **Original**: कर दिया और कहा--ये सेनाएँ युद्ध करेंगी; राजाकों भगा दीजिये। सर्वज्ञ! मायासे विमुग्ध-
- **Translation**: 

---

### Verse 15 (Vaivtpuran 24.7063)
- **Original**: आप वहाँ मत जाइये।' उस सामग्रीसे सम्पन्न चित्त होकर आप क्यों रो रहे हैं ? अरे ! ये संयोग-
- **Translation**: 

---

### Verse 16 (Vaivtpuran 24.7064)
- **Original**: होनेके कारण मुनिको महान हर्ष प्राप्त हुआ। इधर वियोग तो कालकृत हैं, आत्मकृत नहीं हैं। आप
- **Translation**: 

---

### Verse 17 (Vaivtpuran 24.7065)
- **Original**: राजाद्वारा भेजे गये भृत्यने लौटकर राजाकों सारा मेरे कौन हैं और मैं आपकौ कौन हूँ--बह
- **Translation**: 

---

### Verse 18 (Vaivtpuran 24.7066)
- **Original**: वृत्तानन बतलाया। कपिलाकी सेनाका वृत्तान्त सम्बन्ध तो कालद्वारा नियोजित है। जबतक यह
- **Translation**: 

---

### Verse 19 (Vaivtpuran 24.7067)
- **Original**: और अपने पक्षकी पराजय सुनकर नुृपश्रेष्ठ सम्बन्ध है तभीतक आप मेरे हैं। मन जबतक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 24.7068)
- **Original**: कार्तवीर्य भयभीत हो गया। उसके मनमें कातरता जिस वस्तुको केवल अपना मानता है और उसपर
- **Translation**: 

---

