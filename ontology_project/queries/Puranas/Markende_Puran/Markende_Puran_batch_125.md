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

### Verse 1 (Markende Puran 0.2481)
- **Original**: उस समय देंबी अपने ज्ञाणोंके समुहोंसे उसके फैके हुए पर्वतोंकों चुर्ण करती हुई बोलीं। बोलते समय उनका मुख पधुके मदसे लाल हो रहा था और बाणों लड़खड़ा रही थी
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2482)
- **Original**: देव्युकाच #37 # गर्ज गर्ज क्षणं पृदढ मश्चु सावत्पिवाष्यहम्‌। प्रयां त्वयरि हतेउतैव गर्णिष्यन्त्याशु देवताः
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2483)
- **Original**: देवीने कहा--
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2484)
- **Original**: ओ मूढ़
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2485)
- **Original**: में जबतक्त मधु पीती हूँ तबतक तू क्षणभरके लिये खून गर्ज ले। मेरे हाथसे यहाँ तेरी मृत्यु हो जानेपर अब शीघ्र ही देवता भी गर्जना करेंगे
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2486)
- **Original**: ऋषिरुदाच
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2487)
- **Original**: 'एघमुजत्या समुत्पत्य सा$5रूज़ा ते महासुरम्‌। पादेनाक़म्य कण्ठे तर शूलेनैनमताडयतू
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2488)
- **Original**: ततः सो5पि यदा55क्रान्तस्तथा निजमुस्वात्तत:। अधव॑निष्क्रान्त एवासीव्देव्या वीर्येण सं॑बृत्त:
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2489)
- **Original**: अर्थनिष्क्रात्त एवासौ युध्यमानों महासुर:। तया पहासिना देध्या शिरश्छिक्षा निपातितः
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2490)
- **Original**: ततो हाहाकृत सर्व दैत्यसैन्यं चनाश ततू। प्रहर्प त्ञ परे जग्पु: सकला देखतायणा:
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2491)
- **Original**: तुष्शुस्तां सुरा देवों सह दिव्गैमहर्षिभि:। जगुर्गन्‍्धर्वपतयों. भनृतुश्चाप्सरोगणा;
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2492)
- **Original**: ऋषि कहते हैं--
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2493)
- **Original**: यों कहकर देती चंध+ 197 77577 # 4 6644:5 72795 057 48 64623 :2 55704 4 उछली और उस महादैत्यके ऊपर चढ़ गयीं। फिर अपने पैरसे उसे दबाकर उन्होंने शूलसे उसके कण्ठमें आघात क्िया। [ उनके पैरसे दत्ना होनेपर भी मत्तियासुर अपने मुखसे दूसरे रूपसें बाहर होने लगा]
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2494)
- **Original**: अभी आधे शरीरसे ही वह बाहर निकलते पाया था क्रि देवोने अपने ग्रभावसे उसे रोक दिया
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2495)
- **Original**: आशआ निकला होनेपर भी बह महादैत्य देवीसे युद्ध करने ज्वगां। तन्र देवी बहुत बड़ी तलबारसे उसका मस्तक काट गिएया।
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2496)
- **Original**: फिर तो हाहाकार करदी हुई दैत्थोंकों सारे सेना भाग गयी तथा सम्पूर्ण देखता अत्यन्त प्रसन्न हो गये
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2497)
- **Original**: देवताओंने दिव्य महर्षियोंक साथ दुर्गदेबीका स्तवन किया। गम्धर्वराज गात करते लो तथा अप्सराएँ नृत्य करने लगीं
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2498)
- **Original**: ज्ंति ओमर्कण्डेय्पूदणे सावार्णिके अन्वत्तरे देकीमफ़ाा्म्वे महिषातुररयों रण उ्तीस्तेड ध्याव: 43 अ हकाच है, ए्लोका: 41. एयम्‌ 44, एउग्ग्रॉटित:# 2170 बस प्रकार श्रीपार्कण्ठेचपुराणमें स्रावर्णिक्त मन्वन्तरकी कथाके अन्तर्गत देजी-माहात्प्यमें *घहिषासुरं यंध' नापक तीसरा अध्याय पुरा हुआ
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2499)
- **Original**: हा 27:23 &.. 1. प0-एवात्ति देव्या। 2. फकेसों-फिसी 4िगें इसके चाद-- / #लोक्व मोहवित्या तु शया टेव्या विकशित:
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2500)
- **Original**: *एवं स महिणे नःएं रह्तैन्य: ससुहृद्रण: औलोक्टस्थैस्तदा भूतैर्मठिय विन्पातितें। जयेत्युक्त ज़तः राज: सदेवासुरतानये:
- **Translation**: 

---

