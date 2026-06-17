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

### Verse 1 (Vaivtpuran 543.12614)
- **Original**: गये। उन्होंने सौ व्र्षोत्क उस उत्कृष्ट मन्त्रका वेदोंके बीजरूप हैं। इसलिये ब्रह्ममीज कहलाते
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12615)
- **Original**: जप किया। सती राधिके! तदनन्तर तुमने ही हैं; आपको मेरा प्रणाम है। मुनिको प्रत्यक्ष दर्शन देकर उन्हें वर दिया--' वत्स ! इस प्रकार स्तुति करके शिवको प्रणाम तुम्हें निश्रयः ही महाज्ञानी पुत्रकी प्राप्ति करनेके पश्चात्‌ मुनीश्वर असित उनके सामने खड़े
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12616)
- **Original**: होगी।' यह वर देकर तुम पुनः गोलोकमें मेरे हो गये और दीनकी भाँति नेत्रोंसे आँसू बहाने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12617)
- **Original**: पास चली आयीं। तदनन्तर यथासमय भगवान्‌ लगे। उनके सम्पूर्ण शरीरमें रोमाक्न हो आया।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12618)
- **Original**: शिवके अंशसे असितके एक पुत्र हुआ, जो जो असितद्वारा किये गये महात्मा शंकरके इस
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12619)
- **Original**: कामदेवके समान सुन्दर था। उसका नाम हुआ स्तोत्रका प्रतिदिन भक्तिभावसे पाठ करता और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12620)
- **Original**: देवल। देवल त्रह्मनिष्ठ महात्मा हुए। उन्होंने राजा एक वर्षतक नित्य हविष्य खाकर रहता है--उसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12621)
- **Original**: सुयज्ञकी सुन्दी कन्या रत्रमालावतीको, जो ज्ञानी, चिरञ्ञीवी एवं वैष्णव पुत्रकी प्राप्ति होती
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12622)
- **Original**: सबका मन मोह लेनेवाली थी, विवाहकी विधिसे है। जो धनाभावसे दुःखी हो, वह धनाढ्य और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12623)
- **Original**: सानन्द ग्रहण किया। दीर्घकालतक पत्नीके साथ जो मूर्ख हो, वह पण्डित हो जाता है। पत्नीहीन
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12624)
- **Original**: रहकर कालान्तरमें मुनिवर देवल संसारसे विरक्त पुरुषकों सुशीला एवं पतिक्नता पत्नी प्राप्त होती
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12625)
- **Original**: हो गये और सारा सुख छोड़कर धर्ममें तत्पर है तथा वह इस लोकमें सुख भोगकर अन्तमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12626)
- **Original**: हो श्रीहरिके चिन्तनमें लग गये। एक समय भगवान्‌ शिवके समीप जाता है। पूर्वकालमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12627)
- **Original**: रात्रिमें वे विरक्त तपोधन शय्यासे उठे और ब्रह्माजीने यह उत्तम स्तोत्र प्रचेताकों दिया था
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12628)
- **Original**: कमनीय गन्धमादन पर्वतपर तपस्याके लिये चले और प्रचेताने अपने पुत्र असितकों। गये। उनकी पत्नीकी जब निद्रा टूटी, तब वह श्रीकृष्ण कहते हैं--मुनिका यह स्तोत्र
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12629)
- **Original**: सती अपने स्वामीकों वहाँ न देख विरहग्रिसे सुनकर भक्तवत्सल भगवान्‌ शंकर स्वयं ही अपने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12630)
- **Original**: दग्ध हो शोकवश अत्यन्त विलाप करने लगी। भक्त ब्राह्मणसे बोले। वह उठकर कभी खड़ी होती और कभी पछाड़ शंकरजीने कहा--मुनिश्रेष्ठ! धैर्य धारण खाकर गिरती थी। रत्रमालावती बारंबार उच्चस्वरसे करो। मैं तुम्हारी इच्छाकों जानता हूँ; अत: सत्य
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12631)
- **Original**: रोदन करने लगी। तपे हुए पात्रमें पड़े हुए कहता हूँ। तुम्हें मेरे अंशसे मेरे ही समान पुत्र धान्यकी जो दशा होती है, वही दशा उस समय प्राप्त होगा। इसके लिये मैं तुम्हें एक ऐसा मन्त्र
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12632)
- **Original**: उसके मनकी थी। उस सुन्दरीने खाना-पीना दूँगा, जिसकी कहीं तुलना नहीं है तथा जो सबके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12633)
- **Original**: छोड़कर प्राणोंका परित्याग कर दिया। उसके लिये परम दुर्लभ है। पुत्रने उसका दाह-संस्कार आदि पारलौकिक यों कहकर भगवान्‌ शिवने असितमुनिकों
- **Translation**: 

---

