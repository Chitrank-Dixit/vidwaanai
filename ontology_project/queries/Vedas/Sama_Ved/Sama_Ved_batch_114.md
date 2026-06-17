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

### Verse 1 (Sama Ved 0.2261)
- **Original**: 870.अभि ब्रह्मीरनूषत यहीर्ऋतस्य मातर: । मर्जयन्तीर्दिव: शिशुम्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2262)
- **Original**: अन्तरिक्ष से उत्पन सोम को पवित्र करने के लिए यज्ञों में विशिष्ट वेदमंत्रों द्वारा स्‍्तवन किया जाता है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2263)
- **Original**: 871.राय: समुद्रां श्रतुरोस्मभ्य॑ सोम विश्वतः
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2264)
- **Original**: आ पवस्व सहस्रिण:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2265)
- **Original**: हे सोमदेव ! हमारी हजारों इच्छाओं की पूर्ति के लिए, ऐश्वर्य से परिपूर्ण, उलति के चारों समुद्र (धर्म, अर्थ, काम, मोक्ष आदि साधन) हमें हस्तगत कराएँ
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2266)
- **Original**: <872.सुतासो मधुमत्तमा: सोमा इन्द्राय मन्दिन: । पवित्रवन्तों अक्षरं देवान्‌ गच्छन्तु वो मदा:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2267)
- **Original**: अत्यन्त मधुर, आनन्दवर्द्धक, शुद्ध हुआ सोमरस, कलश में इन्द्रदेव के लिए स्नवित होता है । हे सोम राजा ! आपका रस देवशव्तियों के लिए आनन्ददायक हो
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2268)
- **Original**: 873.इन्दुरिन्द्राय पवत इति देवासो अब्ुवन्‌। बाचस्पतिर्मखस्यते विश्वस्येशान ओजसः
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2269)
- **Original**: स्तोताओं के अनुसार सोमरस इस्द्रदेव के लिए शोधित किया जाता है । ज्ञानरक्षक, सर्वसमर्थ सोम, यज्ञ में प्रयुक्त होता है
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2270)
- **Original**: 874.सहस्नथार: पवते समुद्रो वाचमीड्डुयः । सोमस्पती रयीणां सखेन्द्रस्थ दिवेदिवे
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2271)
- **Original**: वाणी का प्रेरक, ऐश्वर्यवान्‌ इन्द्रदेव का मित्र, जल में मिश्रित सोम सहखरों धाराओं से प्रतंदिन कलश में शोधित होता है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2272)
- **Original**: 875.पवित्रं ते विततं ब्रह्मणस्पते प्रभुर्गात्राणि पर्येषि विश्वतः । अतप्ततनूर्न तदामों अश्नुते थ्रुतास इद्बहन्तः सं तदाशत
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2273)
- **Original**: हे मंत्रों के स्वामी सोमदेव ! आपका शुद्ध हुआ भाग सब जगह व्याप्त है । सामर्थ्यवान्‌ साधकों को ही आप उपलब्ध होते हैं। परिपक्व तपस्वी साधक यज्ञ करते हुए आपको प्राप्त करते हैं । शरीर को तप से बिना तपाये, आपका सुख कोई नहीं प्राप्त कर सकता
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2274)
- **Original**: 876.तपोष्पवित्र॑ विततं दिवस्पदे3र्चन्तो अस्य तन्तवो व्यस्थिरन्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2275)
- **Original**: अवन्त्यस्थ पवितारमाशवो दिव: पृष्ठमधि रोहन्ति तेजसा
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2276)
- **Original**: सोम के पवित्र अंग शत्रु को संताप देने के लिए च्ुलोक में फैले हैं। इनकी चमकती हुई रश्मियाँ चुलोक के पृष्ठ भाग पर विशेष रीति से स्थिर हो गई हैं। यह रश्थियाँ याञ्ञिकों की रक्षा करती हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2277)
- **Original**: उत्तराचिके चतुर्थोंध्याव: 47 - 877. अरूरुचदुषस: पृश्निरग्रिय उक्षा मिमेति भुवनेषु वाजयु: । मायाविनो ममिरे अस्य मायया नृचक्षस: पितरो गर्भमा दधु:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2278)
- **Original**: ग्रहों में अग्रणी सूर्यटेव प्रकाशित होकर सभी लोकों में अपनी किरणें फैलाते हैं। समस्त संसार को अन्नादि प्रदान करते हैं । सबको प्रकाशित करने वाली किरणें, गर्भ के समान जल को (अदृश्यरूप से) धारण करती हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2279)
- **Original**: इति पञ्मम: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2280)
- **Original**: ऊके के
- **Translation**: 

---

