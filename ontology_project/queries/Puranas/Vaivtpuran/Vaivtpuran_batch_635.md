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

### Verse 1 (Vaivtpuran 63.5580)
- **Original**: पम्पे! चम्पे! गोमति! पद्मावति! त्रिपर्णाशे! फल प्रदान करनेवाली हो । तुम परमात्मा श्रीकृष्णकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 63.5581)
- **Original**: विपाशे! विरजे! प्रभे! शतहृदे! तथा चेलगड़्े! सर्वशक्तिस्वरूपा हो। जन्म, मृत्यु, जगा और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 63.5582)
- **Original**: आपलोग इस जलमें निवास करें। व्याधिका अपहरण करनेवाली परात्पपा हो।। तत्पश्चात्‌ उस जलमें तुलसी और चन्दनसे . सुखदायिनी, मोक्षदायिनी, भद्रा (कल्याणकारिणी)
- **Translation**: 

---

### Verse 4 (Vaivtpuran 63.5583)
- **Original**: अग्नि, सूर्य, चन्द्रमा, विष्णु, बरुण तथा शिव--इन तथा सदा श्रीकृष्णभक्ति प्रदान करनेवाली हो।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 63.5584)
- **Original**: छ: देवताओंकी पूजा करे । फिर उस जलसे समस्त महामाये! नारायणि! दुर्गे! तुम दुर्गतिका नाश
- **Translation**: 

---

### Verse 6 (Vaivtpuran 63.5585)
- **Original**: नैवेद्योंका प्रोक्षण करे। इसके बाद एक-एक करके करनेवाली हो। दुर्गा नामके स्मरणमात्रसे यहाँ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 63.5586)
- **Original**: सोलह उपचार समर्पित करे। आसन, वसन, पाद्य, मनुष्योंका दुर्गम कष्ट दूर हो जाता है। स््रानीय, अनुलेपन, मधुपर्क, गन्ध, अर्घ्य, पुष्प, इस प्रकार परिहार-स्तवन करके साधक
- **Translation**: 

---

### Verse 8 (Vaivtpuran 63.5587)
- **Original**: अभीष्ट नैवेद्य, आचमनीय, ताम्बूल, रत्नमय भूषण, देवीके बायें भागमें तिपाईके ऊपर शड्ख रखे।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 63.5588)
- **Original**: धूप, दीप और शब्या-ये सोलह उपचार हैं। उसमें जल भर दे और दूर्वा, पुष्प तथा चन्दन (आसन) शंकरप्रिये ! अमूल्य रक्रोंद्वारा निर्मित डाल दे। तत्पश्चात्‌ उसे दाहिने हाथसे पकड़कर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 63.5589)
- **Original**: तथा नाना प्रकारके चित्रोंद्वारा शोभित श्रेष्ठ सिंहासन मनुष्य इस तरह मन्त्र पढ़े। ग्रहण करो। (वस्त्र) शिवे! असंख्य सूत्रोंसे बने “हे शद्भु! तुम पवित्र वस्तुओंमें परम पवित्र
- **Translation**: 

---

### Verse 11 (Vaivtpuran 63.5590)
- **Original**: हुए तथा ईश्वरकी इच्छासे निर्मित प्रज्बलित अग्रिद्वारा हो, मड्भरलोंके भी मदड्भल हो। पूर्वकल्पमें शुद्ध किया हुआ दिव्य वस्त्र स्वीकार करो। शह्डुचूडसे तुम्हारी उत्पत्ति हुई, इसलिये परम
- **Translation**: 

---

### Verse 12 (Vaivtpuran 63.5591)
- **Original**: (पाद्य) दुर्गे! बहुमूल्य रत्रमय पात्रमें रखे हुए पवित्र हो।' इस विधिसे अर्घ्यपात्रकी स्थापना
- **Translation**: 

---

### Verse 13 (Vaivtpuran 63.5592)
- **Original**: निर्मल गड्राजलको पैर धोनेके लिये पाद्यके रूपमें करके दिद्वान्‌ पुरुष उसे देवीको अर्पित करे।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 63.5593)
- **Original**: ग्रहण करो। (स््रानीय) परमेश्वरि! सुगन्धित आँवलेका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 63.5594)
- **Original**: स्रिग्ध द्रव और परम दुर्लभ सुपक्व विष्णुतैल
- **Translation**: 

---

### Verse 16 (Vaivtpuran 63.5595)
- **Original**: उत्तम दिव्य पर्यड्डू रत्नोंके सारभागसे निर्मित हुआ स्रानीय सामग्रीके रूपमें प्रस्तुत है। इसे स्वीकार
- **Translation**: 

---

### Verse 17 (Vaivtpuran 63.5596)
- **Original**: है। इसपर गद्दा है और वह महीन वस्त्रकी चादरसे करो। (अनुलेपन) जगदम्ब ! कस्तूरी और कुछुमसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 63.5597)
- **Original**: ढका हुआ है। तुम इस शय्याकों स्वीकार करो। मिश्रित सुगन्धित चन्दनद्रव सुवासित अनुलेपनके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 63.5598)
- **Original**: मुने! इस प्रकार दुर्गदेबीका पूजन करके रूपमें समर्पित है। इसे ग्रहण करों। (मधुपर्क)
- **Translation**: 

---

### Verse 20 (Vaivtpuran 63.5599)
- **Original**: उन्हें पुष्पाज्नलि चढ़ावे। तदनन्तर देवीकी सहचरी महादेवि! रज्नपात्रमें स्थित परम पवित्र एवं परम
- **Translation**: 

---

