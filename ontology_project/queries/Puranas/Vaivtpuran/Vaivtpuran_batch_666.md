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

### Verse 1 (Vaivtpuran 67.6115)
- **Original**: शंकरजीकों ग्रहण किये जाते देखकर पार्वतीके अपने स्वामीको लौटा लेना। यह बात श्रुतिसम्मत
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.6116)
- **Original**: कण्ठ, ओठ और तालु सूख गये। वे शरीर छोड़ है; क्योंकि जैसे स्वामी यज्ञपत्नीका दान करनेके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.6117)
- **Original**: देनेके लिये उद्यत हो गयीं। उस समय वे मन- लिये सदैव समर्थ है, उसी तरह यज्ञपत्री भी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.6118)
- **Original**: ही-मन सोचने लगीं कि यह कैसी कठिन बात स्वामीकों दे डालनेकी अधिकारिणी है। हुई कि न तो अभीष्टदेवका दर्शन मिला और सभाके बीच यों कहकर नारायण वहीं
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.6119)
- **Original**: न ब्रतका फल हो प्राप्त हुआ। इसी बीच अन्तर्धान हो गये। इसे सुनकर सभी सभासद्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.6120)
- **Original**: पार्वतीसहित देवताओंने आकाशमें एक परमोत्कृष्ट हर्षविभोर हो गये तथा हर्ष-गढ़द हुई पार्वती
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.6121)
- **Original**: तेजसमूह देखा। उसकी प्रभा करोड़ों सूर्योंकी दक्षिणा देनेको उद्यत हुईं। तदनन्तर शिवाने [ प्रभासे उत्कृष्ट थी, वह दसों दिशाओंकों प्रज्बलित हवनकी पूर्णाहुति करके शिवको दक्षिणारूपमें दे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.6122)
- **Original**: कर रहा था और सम्पूर्ण देवताओंसे युक्त कैलास दिया और उधर सनत्कुमारजीने उस देवसभामें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.6123)
- **Original**: पर्वतको तथा सबको आच्छादित कर रहा था। 'स्वस्ति' ऐसा कहकर दक्षिणा ग्रहण कर ली।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.6124)
- **Original**: उसकी मण्डलाकृति बड़ी विस्तृत थी। भगवान्‌के उस समय भयभीत होनेके कारण दुर्गाका कण्ठ,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.6125)
- **Original**: उस तेजको देखकर देवता लोग क्रमश: उनकी ओठ और तालु सूख गया था, वे हाथ जोड़कर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.6126)
- **Original**: स्तुति करने लगे। दुःखी हृदयसे ब्राह्मणसे बोलीं। विष्णुने कहा--भगवन्‌ ! यह जो महाविराट्‌ पार्वतीजीने कहा--विप्रवर! 'गौका मूल्य
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.6127)
- **Original**: है, जिसके रोमछिद्रोमें सभी ब्रह्माण्ड वर्तमान हैं, मेरे पतिके बराबर है'--ऐसा बेदमें कहा गया
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.6128)
- **Original**: वह जब आपका सोलहवाँ अंश है, तब हम है, अतः मैं आपको एक लाख गाौएँ प्रदान
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.6129)
- **Original**: लोगोंकी क्या गणना है? करूँगी। आप मेरे स्वामीको लौटा दीजिये। पतिक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.6130)
- **Original**: . ब्रह्माले कहा--परसेश्वर ! जो वेदोंके उपयुक्त मिल जानेपर मैं ब्राह्मणॉंको अनेक प्रकारकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.6131)
- **Original**: दृश्य है, उसका प्रत्यक्ष दर्शन करने, स्तवन करने दक्षिणाएँ बाँटूँगी। (अभी तो मैं आत्महीन हूँ,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.6132)
- **Original**: तथा वर्णन करनेमें मैं समर्थ हूँ; परंतु जो वेदोंसे ऐसी दशामें) भला, आत्मासे रहित शरीर कौन-
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.6133)
- **Original**: परे है, उसकी मैं क्‍या स्तुति करूँ? सा कर्म करनेमें समर्थ हो सकता है? श्रीमहादेवजीने कहा--भगवन्‌! जो सबके सनत्कुमारजी बोले--देवि! मैं ब्राह्मण हूँ।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.6134)
- **Original**: लिये अनिर्वचनीय, स्वेच्छामय, व्यापक और मुझे एक लाख गौओंसे क्‍या प्रयोजन है और
- **Translation**: 

---

