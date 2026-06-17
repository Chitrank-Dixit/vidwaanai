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

### Verse 1 (Nard Puran 224.4121)
- **Original**: ऊपर जाती, कभी नीचे आती और कभी बीचमें परम स्वरूप है, वह भाव और अभावसे रहित,
- **Translation**: 

---

### Verse 2 (Nard Puran 224.4122)
- **Original**: ठहरी रहती है, उसी प्रकार मैं कर्मरूपी रज्जुमें निर्लेप, निर्मल, सूक्ष्म, कूटस्थ, अचल, ध्रुव,
- **Translation**: 

---

### Verse 3 (Nard Puran 224.4123)
- **Original**: बैधकर दैवयोगसे ऊपर, नीचे तथा मध्यवर्ती समस्त उपाधियोंसे विमुक्त और सत्तामात्ररूपसे
- **Translation**: 

---

### Verse 4 (Nard Puran 224.4124)
- **Original**: लोकमें भटकता रहता हूँ। इस प्रकार यह संसार- स्थित है। प्रभो! उसे देवता भी नहीं जानते, फिर
- **Translation**: 

---

### Verse 5 (Nard Puran 224.4125)
- **Original**: चक्र बड़ा ही भयानक एवं रोमाझकारी है। मैं मैं कैसे जान सकता हूँ। उससे भिन्न जो आपका
- **Translation**: 

---

### Verse 6 (Nard Puran 224.4126)
- **Original**: इसमें दीर्घकालसे घूम रहा हूँ, किंतु कभी मुझे दूसरा स्वरूप है, वह पीताम्बरधारी और चार
- **Translation**: 

---

### Verse 7 (Nard Puran 224.4127)
- **Original**: इसका अन्त नहीं दिखायी देता। समझमें नहीं भुजाओंसे युक्त है। उसके हाथोंमें शट्ल, चक्र
- **Translation**: 

---

### Verse 8 (Nard Puran 224.4128)
- **Original**: आता, अब मैं क्‍या करूँ ? हरे! मेरी सम्पूर्ण और गदा सुशोभित हैं। वह मुकुट और अद्भद
- **Translation**: 

---

### Verse 9 (Nard Puran 224.4129)
- **Original**: इन्द्रियाँ व्याकुल हो गयी हैं। मैं शोक और तृष्णासे धारण करता है। उसका वक्ष:स्थल श्रीवत्सचिह्से
- **Translation**: 

---

### Verse 10 (Nard Puran 224.4130)
- **Original**: आक्रान्त होकर अब कहाँ जाऊँ ? मेरी चेतना लुप्त युक्त है तथा वह वनमालासे विभूषित रहता है।
- **Translation**: 

---

### Verse 11 (Nard Puran 224.4131)
- **Original**: हो रही है। देव! इस समय व्याकुल होकर मैं देवता तथा आपके अन्यान्य शरणागत भक्त उसीको । आपकी शरणमें आया हूँ। श्रीकृष्ण! मैं संसार- पूजा करते हैं। देव! आप सम्पूर्ण देवताओंमें श्रेष्ठ
- **Translation**: 

---

### Verse 12 (Nard Puran 224.4132)
- **Original**: समुद्रमें डूबकर दुःख भोग रहा हूँ, मुझे बचाइये। एबं भक्तोंको अभय देनेवाले हैं। मनोहर कमलके
- **Translation**: 

---

### Verse 13 (Nard Puran 224.4133)
- **Original**: जगन्नाथ ! यदि आप मुझे अपना भक्त मानते हैं तो समान नेत्रोंवाले प्रभो! मैं विषयोंके समुद्रमें डूबा
- **Translation**: 

---

### Verse 14 (Nard Puran 224.4134)
- **Original**: मुझपर कृपा कौजिये। आपके सिवा दूसरा कोई हूँ, आप मेरी रक्षा कीजिये। लोकेश! मैं आपके
- **Translation**: 

---

### Verse 15 (Nard Puran 224.4135)
- **Original**: ऐसा बन्धु नहीं है जो मेरी तरफ खयाल करेगा। सिवा और किसीको नहीं देखता, जिसकी शरणमें
- **Translation**: 

---

### Verse 16 (Nard Puran 224.4136)
- **Original**: देव! प्रभो! आप-जैसे स्वामीकी शरणमें आकर जाऊँ। कमलाकान्त! मधुसूदन! आप मुझपर
- **Translation**: 

---

### Verse 17 (Nard Puran 224.4137)
- **Original**: अब मुझे जीवन-मरण अथवा योगक्षेमके लिये प्रसन्न होइये। मैं बुढ़ापे और सैकड़ों व्याधियोंसे
- **Translation**: 

---

### Verse 18 (Nard Puran 224.4138)
- **Original**: कहों भी भय नहीं होता। हरे! अपने कर्माँसे नारायण ! आपको नमस्कार है। आप मुझ शरणागतकी
- **Translation**: 

---

### Verse 19 (Nard Puran 224.4139)
- **Original**: संक्षिप्त नारदपुराण बँधे रहनेके कारण मेरा जहाँ-कहीं भी जन्म हो,
- **Translation**: 

---

### Verse 20 (Nard Puran 224.4140)
- **Original**: नहीं हैं, फिर मानवी बुद्धिसे मैं आपकी स्तुति वहाँ सर्वदा आपमें मेरी अविचल भक्ति बनी रहे।
- **Translation**: 

---

