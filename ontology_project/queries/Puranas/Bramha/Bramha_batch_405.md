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

### Verse 1 (Bramha 0.8081)
- **Original**: 388 * संक्षिप्त ब्रह्मपुराण * उस चाण्डालकी आयुका अधिकांश भाग बीत गया।
- **Translation**: 

---

### Verse 2 (Bramha 0.8082)
- **Original**: कलड्ड देने, वनमें आग लगाने, गौको हत्या करने, एक दिन चैत्रके कृष्णपक्षकी एकादशी तिथिको वह
- **Translation**: 

---

### Verse 3 (Bramha 0.8083)
- **Original**: ब्राह्मणाधम होने और बड़े भाईके अविवाहित रहते भगवान्‌ विष्णुकी सेवा करनेके लिये जंगली पुष्पोंका
- **Translation**: 

---

### Verse 4 (Bramha 0.8084)
- **Original**: स्वयं विवाह कर लेनेपर जो पाप लगता है तथा संग्रह करनेके निमित्त भक्तिपूर्वक उत्तम वनमें गया।
- **Translation**: 

---

### Verse 5 (Bramha 0.8085)
- **Original**: भ्रूणहत्या करनेवाले मनुष्योंको जिस पापको प्राप्ति होती क्षिप्राके तटपर महान्‌ वनके भीतर एक बहेड़ेका वृक्ष
- **Translation**: 

---

### Verse 6 (Bramha 0.8086)
- **Original**: है--अधथवा यहाँ बहुत-से शपथोंका वर्णन करनेसे क्या था। उसके नीचे पहुँचनेपर किसी राक्षसने उस
- **Translation**: 

---

### Verse 7 (Bramha 0.8087)
- **Original**: लाभ। राक्षस! एक भयंकर शपथ सुन लो; यद्यपि बह चाण्डालको देखा और भक्षण करनेके लिये पकड़
- **Translation**: 

---

### Verse 8 (Bramha 0.8088)
- **Original**: कहने योग्य नहीं है तो भी कहता हूँ---अपनी कन्याको लिया। यह देख चाण्डालने उस राक्षससे कहा--' भद्र
- **Translation**: 

---

### Verse 9 (Bramha 0.8089)
- **Original**: बेचकर जीविका चलानेवाले, झूठी गवाही देने एवं आज तुम मुझे न खाओ, कल प्रातःकाल खा लेना।
- **Translation**: 

---

### Verse 10 (Bramha 0.8090)
- **Original**: यज्ञक अनधिकारीसे यज्ञ करानेताले मनुष्योंको जिस मैं सत्य कहता हूँ, फिर तुम्हारे पास लौट आऊँगा।
- **Translation**: 

---

### Verse 11 (Bramha 0.8091)
- **Original**: पापका भागी होना पड़ता है तथा, संन्यासी और राक्षस! आज मेरा बहुत बड़ा कार्य है, अत: मुझे / ब्रह्मचारीको कामभोगमें आसक्त होनेपर जिस पापकी छोड़ दो। मुझे भगवान्‌ विष्णुकी सेवाके लिये रात्रिमें
- **Translation**: 

---

### Verse 12 (Bramha 0.8092)
- **Original**: प्राप्ति होती है, उक्त सभी पापोंसे मैं लिप्त होऊँ, यदि जागरण करना है। तुम्हें उसमें विध्न नहीं डालना
- **Translation**: 

---

### Verse 13 (Bramha 0.8093)
- **Original**: तुम्हारे पास लौटकर न आऊँ।' चाहिये। ब्रह्मराक्षस! सम्पूर्ण जगत॒का मूल सत्य ही
- **Translation**: 

---

### Verse 14 (Bramha 0.8094)
- **Original**: . चाण्डालकी यह बात सुनकर भ्रह्मणक्षसको बड़ा है, अत: मेरी बात सुनो। मैं सत्यकी शपथ खाकर
- **Translation**: 

---

### Verse 15 (Bramha 0.8095)
- **Original**: विस्मय हुआ। उसने कहा--जाओ, सत्यके द्वारा कहता हूँ, पुन: तुम्हारे पास लौट आऊँगा। परायी
- **Translation**: 

---

### Verse 16 (Bramha 0.8096)
- **Original**: अपनी की हुई प्रतिज्ञुका पालन करना।' राक्षसके स्त्रियोंके पास जाने और परायें धनको हड़प लेनेबाले
- **Translation**: 

---

### Verse 17 (Bramha 0.8097)
- **Original**: यों कहनेपर चाण्डाल फूल लेकर भगवान्‌ विष्णुके मनुष्योंको जिस पापकी प्राप्ति होती है, ब्रह्महत्योरे,
- **Translation**: 

---

### Verse 18 (Bramha 0.8098)
- **Original**: मन्दिरपर आया। उसने सभी फूल ब्राह्मणको दे शराबी और गुरुपत्नीगामी तथा शुद्रजातीय स्त्रीसे
- **Translation**: 

---

### Verse 19 (Bramha 0.8099)
- **Original**: दिये। ब्राह्मणने उन्हें जलसे धोकर उनके द्वारा सम्बन्ध रखनेवाले द्विजको जो पाप होता है, कृतघ्न,
- **Translation**: 

---

### Verse 20 (Bramha 0.8100)
- **Original**: भगवान्‌ विष्णुका पूजन किया और अपने घरकी राह मित्रघाती, दुबारा ब्याही हुई स्त्रीके पति, क्रूरतापूर्ण
- **Translation**: 

---

