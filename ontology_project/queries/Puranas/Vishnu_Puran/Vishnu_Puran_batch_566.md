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

### Verse 1 (Vishnu Puran 0.11301)
- **Original**: 7 हतेषु तेषु बाणो5पि रथस्थस्तद्वधोद्यत: । युध्यमानो यथाशक्ति यदुबीरेण निर्जितः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11302)
- **Original**: 8 मायया युयुधे तेन स तदा मन्त्रियोदित: । ततस्त॑ पन्नगास्रेण बब्ध यदुनन्दनम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11303)
- **Original**: 9 द्वारवत्यों क्न यातो5सावनिरुद्धेति जल्पताम्‌ । यदूनामाचचक्षे त॑ बद्धं बाणेन नारदः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11304)
- **Original**: 10 ते शोणितपुरं नीत॑ श्रुत्वा विद्याविदग्धया । योषिता प्रत्ययं जम्मुर्यादवा नामरैरिति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11305)
- **Original**: 19 ततो गरुडमारुह्म स्मृतमात्राग्त हरिः । श्रीपराशरजी ओस्डे--हे मैत्रेय! एक बार बाणासुरने भी भगवान्‌ त्रिलोचनको प्रणाम करके कहा था कि हे देव ! बिना युद्धके इन हजार भुजाओसे मुझे बड़ा ही स्वेद हो रहा है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11306)
- **Original**: क्या कभी मेरी इन भुजाओंकों सफल करनेवाए्त्र युद्ध होगा ? भव्म बिना युद्धके इन भाररूप भुजाओँसे मुझे लाभ ही क्या है ?
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11307)
- **Original**: अश्रीदाद्डरुजो खोले--हे बाणासुर
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11308)
- **Original**: जिस समय तेरी मयूर-चिह्नवाली ध्वजा टूट जायगी उसी समय तेरे सामने मांसभोजी यक्ष-पिश्ञायादिकों आनन्द देनेवाला युद्ध उपस्थिति होगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11309)
- **Original**: श्रीपराशहरजी जोले--तदनन्तर, . वरदायक औ्रीशकरको प्रणामकर बाणासुर अपने घर आया और फिर कालान्तरमें उस ध्वजाको टूटी देखकर अति आनन्दित हुआ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11310)
- **Original**: इसी समय अप्सराश्रेष्ठ चित्रलेखा अपने योगबलसे अनिरुझधको वहाँ ले आयी
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11311)
- **Original**: अनिरुद्धको कन्यात्तःपुरमें आकर उषाके साथ र्मण करता जान अन्तःपुररक्षकोनि सम्पूर्ण वुत्तात्त दैल्थराज बाणासुरसे कह दिया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11312)
- **Original**: तब महावीर बाणासुरने अपने सेवकॉको उससे युद्ध करनेकी आज्ञा दी; किंतु शत्रु-दमन अनिरुद्धने अपने सम्मुख आनेपर उस सस्पूर्ण सेनाव्यरे एक लोहमय दण्डसे मार डालता
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11313)
- **Original**: अपने सेवकॉके मारे जानेपर बाणासुर अनिरुद्धको मार डालनेको इच्छासे रथपर चढ़कर उनके साथ युद्ध करने लगा; किंतु अपनी शक्तिभर युद्ध करनेपर भी वह यदुवीर अनिरुद्धजीसे परास्त हो गया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11314)
- **Original**: तब बह मन्ल्रियोंकी अरणासे मायापूर्वक युद्ध करने रूगा और यदुननन्‍्दन अनिरुद्धको नागपाशसे बाँध लिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11315)
- **Original**: इधर द्वारकापुरीमें जिस समय समस्त यादवोमें यह चर्चा हो रही थी कि 'अनिरुद्ध कहाँ गये ?' उसी समय देवर्षि नारदने उनके बाणासुरद्वारा बाँधे जानेकी सूचना दी
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11316)
- **Original**: नारदजीके मुखसे योगविद्यार्में निपुण युवती चित्रलेखाड़ारा उन्हें. शोणितपुर ले जाये गये सुनकर यादवॉको विश्वास हो गया कि देवताओंने उन्हें नहों बलप््युम्रसहितो बाणस्य प्रययौ पुरम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11317)
- **Original**: चुराया”
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11318)
- **Original**: तज स्मरणमात्रसे उपस्थित हुए गरुडपर + अबतक यादलगण यसह्ठी सोच रहे थे कि पारिजात-हरणसे चिढ़कर देवता ही अनिरुद्धकों चुरा ले गये हैं।
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11319)
- **Original**: आ0 हे ] पञ्षम अंश 399 पुरप्रवेशे प्रमथर्युद्धमासीन्महात्मन: । ययौ बाणपुराभ्याइं नीत्वा तान्सब्ल॒य॑ हरि:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11320)
- **Original**: 13 ततस्त्रिपादस्ब्रिशिरा ज्बरो माहेश्वरों महान्‌। बाणरक्षार्थमभ्येत्व॒युयुधे शार्ड्र्धन्‍्वना
- **Translation**: 

---

