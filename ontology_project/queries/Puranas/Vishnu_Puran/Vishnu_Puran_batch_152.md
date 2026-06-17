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

### Verse 1 (Vishnu Puran 0.3021)
- **Original**: 9 यावन्त: सागरा द्वीपास्तथा वर्षाणि पर्वता: । बनानि सरितः पुर्यो देखादीनां तथा मुने
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3022)
- **Original**: 2 यत्प्रमाणमि्द॑ सर्व॑_यदाधारं॑ वदात्मकम्‌ । संस्थानमस्थ च मुने यथादद्चक्तुमहसि
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3023)
- **Original**: 3 श्रीपय्ज़्र उवाच मैत्रेय. श्रूयतामेतत्सड्लेपाददतो . मम । नास्य वर्षशत्तेनापि वरक्तु शक्यो हि बिस्तर:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3024)
- **Original**: 4 जम्यूप्रक्षाह़्यो द्वीपो शाल्मलश्चापरों द्विज। कुशः क्रौद्धस्तथा शाकः पुष्करश्षैव सप्तम:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3025)
- **Original**: 5 एते द्वीपाः समुद्रेस्तु सप्त सप्तभिरावृताः । लवणेक्षुसुरासर्पिदधिदुग्धजलै;.. समम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3026)
- **Original**: 6 जम्बूद्वीप:प समस्तानामेत्तेषां मध्यसंस्थितः । तस्यापि मेरुमैत्रेय. मध्ये कनकपर्वतः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3027)
- **Original**: 7 चतुरशीतिसाहस्नो योजनैरस्प चोच्छुय:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3028)
- **Original**: 8 प्रविष्टः षोडशाधस्तादद्वार्त्रिशन्यूझ्ि विस्तृत: । श्रीमैत्रेयजी बोले--हे ब्रह्मनू! आपने मुझसे स्वायन्भुबमनुके व॑शका वर्णन किया। अब मैं आफ्के मुखारविन्दसे सम्पूर्ण पृथिवीमण्डलूका विवरण सुनना चाहता हूँ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3029)
- **Original**: हे मुने ! जितने भी सागर, द्वीप, वर्ष, पर्वत, वन, नदियाँ मौर देवता आदिकी पुरियाँ हैं, उन सबका जितना-जितना परिमाण है, जो आधार है, जो उपादान-कारण है और जैसा आकार है, वह सब आप यथावत्‌ वर्णन कीजिये। 2-3
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3030)
- **Original**: श्रीपराइरजी बोले--हे मैत्रेय ! सुनो, मैं इन सब बातॉका संक्षेपसे वर्णन करता हूँ, इनका विस्तारपूर्वक वर्णन तो सौ बर्षमें भी नहीं हो सकता
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3031)
- **Original**: हे द्विज ! जम्बू, प्रक्ष, शाल्मल, कुश, क्रौस, शाक और सातवां पुष्कर--ये सातों द्वीप चारों ओरसे खारे पानी, इक्षुरस, घिरे हुए हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3032)
- **Original**: हे मैत्रेय ! जम्बूद्दीप इन सबके मध्यमें स्थित है और उसके भी बीचों-बीचमें सुवर्णमय सुमेरुपर्वत है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3033)
- **Original**: इसको ऊँचाई चौरासो हजार योजन है और नोचेको ओर यह सोलह हजार योजन पृथिवीमें घुसा हुआ है। इसका विस्तार ऊपरी भागमें बत्तीस हजार योजन है तथा नीचे मूले षोडशसाहस्नरों विस्तारस्तस्थ सर्वशः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3034)
- **Original**: (तलैटीमें) केवल सोलह हजार योजन है। इस प्रकार
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3035)
- **Original**: आ02 ] द्वितीय अं 109 भूषदास्थास्य दौत्पेज्सो कर्णिकाकारसंस्थित:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3036)
- **Original**: 10 हिमवान्हेमकूटश्ल॒ निषधश्चास्थ॒दक्षिणे । नील: श्रेतश्न श्रूड़ी च उत्तरे वर्षपर्वता:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3037)
- **Original**: 19 ल्क्षप्रमाणों द्वौ मध्यौ दशहीनास्तथापरे । सहल्लद्वितयोच्छयास्तावद्विस्तारिणश्ल॒ते
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3038)
- **Original**: 12 भारतं प्रथम यर्ष तत: किम्पुरुष स्मृतम्‌। हरिवर्ष तथैवान्यम्मेरोर्दक्षिणतो द्विज
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3039)
- **Original**: 13 रम्यक चोत्तरं वर्ष तस्वैवानु हिरण्मयम्‌। उत्तरा: कुरवश्चैव यथा थे भारत तथा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3040)
- **Original**: 14 नवसाहस्नमेकैकमेतेषां ह्िजसत्तम । इलाबृते च् तन्मध्ये सौवर्णों मेरुरुच्छूत:
- **Translation**: 

---

