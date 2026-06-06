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

### Verse 1 (Vishnu Puran 0.4921)
- **Original**: इससे गुरु वैशम्पायनजीने क्रोधित होकर महामुनि याज्ञवल्क्यसे कहा--''ओरे आह्राणोंका अपमान करनेवाले ! तूने मुझसे जो कुछ पढ़ा है, वह सब त्याग दे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4922)
- **Original**: तू इन समस्त द्विजश्रेश्नोंको निस्तेज बताता है, मुझे तुझ-जैसे आज्ञा भज्ज- कारी जिष्यसे कोई प्रयोजन नहीं है”
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4923)
- **Original**: याज्यल्ड्यने कहा, “हे द्विज ! मैंने तो भक्तिवश आपसे ऐसा कहा था, मुझे भी आपसे कोई प्रयोजन नहीं है; लीजिये, मैंने आपसे जो कुछ पढ़ा है वह यह मौजूद है''
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4924)
- **Original**: श्रीपराशरजी बोले--ऐसा कह महामुति याज्वल्क्यजीने रुधिरसे भरा हुआ मूर्तिमान्‌ यजुर्वेद उमन करके उन्हें दे दिया; और स्वेच्छछनुसार चले गये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4925)
- **Original**: है द्विज ! याज्जवल्क्‍यद्वाण वमन की हुई उन यजु:श्रुतियोंको अन्य दिष्योने तित्तिर (तीतर) होकर ग्रहण कर छिया, इसल्थ्ये ये सब तैत्तितिय कहलाये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4926)
- **Original**: हे मुनिसत्तम ! जिन घिप्रगणने गुरुको प्रेरणासे अ्रह्महत्या-लिनाशाक ब्रततक। अनुष्ठान किया था, वे सब ब्रताचरणके कारण यजु:ज्ञास्ाध्यायी चरक्राध्यर्यु हुए
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4927)
- **Original**: तदनन्तर, याज्ञजल्क्यने भी यजुर्वेदकी प्राप्तिकी इच्छासे प्राणोंका संयम कर संयतचित्तसे सूर्यभगवान्‌की स्तुति की
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4928)
- **Original**: याज्ञवलक्यजी बोल्ले-- अतुलित तेजस्वी, द्रासस्बरूप तथा वेदत्रयरूप तेजसे सम्पन्न एवं ऋफ्‌, यजुः तथा सामस्वरूप सवितादेवक्त नमस्कार है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4929)
- **Original**: जो अग्रि और चन्द्रमारूप, जगत्‌के कारण और सुुप्न तामक परमतेजको घारण करनेवाले हैं, उन भगवान्‌ धास्करकों नमस्कार है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4930)
- **Original**: कला, काष्टा, निमेष अगदि कालज्ञानके कारण तथा ध्यात् करनेयोग्य परम्रह्मस्वरूप विष्णुमय श्रीसूर्यदेलको नमस्कार है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4931)
- **Original**: जो अपनी फिरणोंसे चद्रमाको पोषित करते हुए देवताओंकों तथा स्वधारूप अमृतसे तृप्त करते हैं, उन तृप्तिरूप सुर्यदेखको नमस्कार 20% 19
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4932)
- **Original**: जो हिम, जकू और उष्णताके कर्ता [अर्थात्‌ शीत, वर्षा और ग्रीष्म आदि ऋतुओंके कारण] है और [जगत्‌का] पोषण करनेवाले हैं, उन त्रिकाल्मूर्ति विधाता भगवान्‌ सूर्यको नमस्कार है । 20
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4933)
- **Original**: जो जगत्पति इस सम्पूर्ण जगत्‌के अन्धकारकों दूर करते हैं, उन सत्वसूर्तिधारी-विवस्थानकों नमस्कार है। 26
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4934)
- **Original**: जिनके उदित हुए बिना मनुष्य सत्कर्ममें अ्रवृत्त नहीं हो सकते और जल शुद्धिका कारण नहीं यप्मिन्ननुदिते तस्मै नमो देवाय भास्वते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4935)
- **Original**: हो सकता, उन भास्वान्देबको नमस्कार है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4936)
- **Original**: 176 अीकिष्णुपुराण [अब्छ स्पृष्टो य्दंशुभिलोंक: क्रियायोम्यो हि जायते। पवित्रताकारणाय तस्मै शुद्धात्मने नमः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4937)
- **Original**: 23 नमः सवित्रे सूर्याय भास्कराय विवस्वते । आदित्यायादिभूताय देवादीनों नमो नम:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4938)
- **Original**: 24 हिरण्पयं रथ यस्य केतवो5मृतवाजिनः । वहन्ति भुवनालोकिचक्षूष ते नमाम्यहम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4939)
- **Original**: 25 औ्रीपताशर उकाच इत्येबमादिभिस्तेन स्तृयमानस्स सै रति: । वाजिरूपधर: प्राह ब्रियतामिति वाड्छितम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4940)
- **Original**: 26 याज्ञवल्क्यस्तदा प्राह प्रणिपत्य दिवाकरम्‌ । यजूंषि तानि मे देहि यानि सन्ति न मे गुरौ
- **Translation**: 

---

