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

### Verse 1 (Vaivtpuran 5.2433)
- **Original**: कब शापसे मुक्त होकर पुनः आपके चरणकमलोंको वे क्रमश: उनसे प्रार्थना करने लगीं। पा सकेंगी ? प्रभो! आप जो इन सरस्वतीसे कह सरस्वतीने कहा--नाथ ! मुझ दुष्टाको पाप,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 5.2434)
- **Original**: रहे हैं कि तुम ब्रह्माके घर सिधारों अथवा गड्जाको ताप और शापसे बचानेके लिये कोई प्रायश्चित्त
- **Translation**: 

---

### Verse 3 (Vaivtpuran 5.2435)
- **Original**: शिवके भवनपर जानेकी आज्ञा दे रहे हैं-- आपके बता दीजिये; जिससे मेरा जन्म और जीवन शुद्ध
- **Translation**: 

---

### Verse 4 (Vaivtpuran 5.2436)
- **Original**: इन बचनोंके लिये मैं आपसे क्षमा चाहती हूँ। हो जाय। भला, आप-जैसे महान्‌ सच्चरित्र
- **Translation**: 

---

### Verse 5 (Vaivtpuran 5.2437)
- **Original**: आप कृपा करके इन्हें ऐसा दण्ड न दें। स्वामीके परित्याग कर देनेपर कहाँ कौन स्त्रियाँ। नारद! इस प्रकार कहकर भगवती लक्ष्मीने जीवित रह सकती हैं? प्रभो! मैं भारतवर्षमें
- **Translation**: 

---

### Verse 6 (Vaivtpuran 5.2438)
- **Original**: अपने स्वामी श्रीहरिके चरण पकड़ लिये, उन्हें योगसाधन करके इस शरीरका त्याग कर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 5.2439)
- **Original**: प्रणाम किया और अपने केशसे भगवान्‌के दूँगी--यह निश्चित है। चरणोंको आवेष्टित करके वे बारंबार रोने लगीं। गड्ढा बोली--जगत्प्रभो! आप किस अपराधसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 5.2440)
- **Original**: भगवान्‌ श्रीहरि सदा भक्तोंपर अनुग्रह करनेवाले मुझे त्याग रहे हैं? मैं जीवित नहीं रह सकूँगी।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 5.2441)
- **Original**: हैं। प्रार्था सुनकर उन्होंने देबी कमलाकों लक्ष्मीने कहा--नाथ! आप सत्त्व-स्वरूप
- **Translation**: 

---

### Verse 10 (Vaivtpuran 5.2442)
- **Original**: हृदयसे चिपका लिया और प्रसन्नमुखसे मुस्कराते हैं। बड़े आश्चर्यकी बात है, आपको कैसे क्षोभ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 5.2443)
- **Original**: हुए कहा। हो गया। आप अपनी इन पत्रियोंपर कृपा भगवान्‌ विष्णु बोले--सुरेश्वरि! कमलेक्षणे ! कौजिये। कारण, श्रेष्ठ स्वामीके लिये क्षमा ही
- **Translation**: 

---

### Verse 12 (Vaivtpuran 5.2444)
- **Original**: मैं तुम्हारो बात भी रखूँगा और अपने बचनकी उत्तम है। मैं सरस्वतीका शाप स्वीकार करके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 5.2445)
- **Original**: भी रक्षा करूँगा। साथ ही तुम तीनोंमें समता अपनी एक कलासे भारतबर्षमें जाऊँगी। परंतु
- **Translation**: 

---

### Verse 14 (Vaivtpuran 5.2446)
- **Original**: कर दूँगा, अतः सुनो। ये सरस्वती कलाके एक प्रभो! मुझे कितने समयतक वहाँ रहना होगा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 5.2447)
- **Original**: अंशसे नदी बनकर भारतवर्षमें जाये, आधे अंशसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 5.18540)
- **Original**: <रैड + संक्षिप्त ब्रह्मवैवर्सपुराण «» गमनाईमपादं॑ यदचक्षु;। सर्वदर्शनम्‌ । हस्तास्यहीन: यद्‌ भोक्त तेजोरूपं नमाम्यहम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 5.18541)
- **Original**: बेदे निरूपितं वस्तु सन्‍्तः शक्ताश्न वर्णितुम्‌। वेदेडनिरूपितं॑ यत्तत्तेजोरूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 5.18542)
- **Original**: सर्वेश॑ यदनीशं यत्‌ सर्वादि यदनादि यत्‌। सर्वात्मकमनात्म॑ यत्तेजोरूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 5.18543)
- **Original**: अहँ विधाता जगतां बेदानां जनकः स्वयम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 5.18544)
- **Original**: पाता श्वर्मों हरो हर्ता स्तोतुं शक्ता न कोठपि यत्‌
- **Translation**: 

---

